from asyncio import threads
import json
import sys
import threading
import queue
from xmlrpc.client import TRANSPORT_ERROR
import pandas as pd
import os
from gitlab2pandas.core import Core


class Extractions(Core):

    def __init__(self, data_root_dir: str, project=None, project_namespace=None, project_name=None, extract_parallel=False) -> None:
        super().__init__(data_root_dir, project, project_namespace, project_name)
        self.extract_parallel = extract_parallel
        self.data_queue = queue.Queue()
        self.consumer_thread = threading.Thread(target=self.gitlab_data_consumer)
        self.log_queue = queue.Queue()
        self.log_serial_thread = threading.Thread(target=self.log_serial_consumer)
        self.log_parallel_thread = threading.Thread(target=self.log_parallel_consumer)
        self.use_feature_whitelist = None
        self.feature_list = []
    
    ### start extractions ###
    def start(self, feature_blacklist = [], feature_whitelist = []):
        if self.project is None:
            raise Exception("Need a project")
        if self.consumer_thread.is_alive():
            raise Exception("Can not extract Data. There is already one extraction running")
        if feature_whitelist != []:
            self.use_feature_whitelist = True
            self.feature_list = feature_whitelist
            if feature_blacklist != []:
                print("Whitelist is used and Blacklist is ignored!")
        elif feature_blacklist != []:
            self.use_feature_whitelist = False
            self.feature_list = feature_blacklist
        else:
            self.use_feature_whitelist = None
        self.consumer_thread.start()
        method_list = [method for method in dir(Extractions) if method.startswith('extract') is True]
        if self.extract_parallel:
            ### parallel ###
            self.log_parallel_thread.start()
            threads = []
            for method in method_list:
                threads.append(threading.Thread(target=getattr(self,method), args=()))
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
        else:
            ### sequential ### 
            self.log_serial_thread.start()
            for method in method_list:
                getattr(self,method)()
        self.data_queue.put((None,None))
        self.consumer_thread.join()
        self.use_feature_whitelist = None
        self.feature_list = []

    def pass_white_black_list(self, feature):
        if self.use_feature_whitelist is None:
            return True
        elif self.use_feature_whitelist and feature in self.feature_list:
            return True
        elif not self.use_feature_whitelist and feature not in self.feature_list:
            return True
        return False

    ### Branches ###
    def extract_branches(self):
        if not self.pass_white_black_list(Core.Features.BRANCHES):
            return
        self.__gitlab_data_producer(self.project, Core.Features.BRANCHES, ["branches", "list"])
        
    ### Commits ###
    def extract_commits(self):
        functions = ["commits", "list"]
        sub_functions = {}
        if self.pass_white_black_list(Core.Features.COMMITS_COMMENTS):
            sub_functions[Core.Features.COMMITS_COMMENTS] = ["comments", "list"]
        if self.pass_white_black_list(Core.Features.COMMITS_REFS):
            sub_functions[Core.Features.COMMITS_REFS] = ["refs"]
        if self.pass_white_black_list(Core.Features.COMMITS_DIFFS):
            sub_functions[Core.Features.COMMITS_DIFFS] = ["diff"]
        if self.pass_white_black_list(Core.Features.COMMITS_STATUSES):
            sub_functions[Core.Features.COMMITS_STATUSES] = ["statuses", "list"]
        if not self.pass_white_black_list(Core.Features.COMMITS):
            if not self.use_feature_whitelist:
                # If the feature is on the blacklist then ignore the feature and its subfeatures
                return
            if sub_functions == {}:
                # If the feature is not on the whitelist then ignore the feature only if no subfeature is on the whitelist
                return
        if sub_functions != {}:
            functions = {
                "attr": functions,
                "sub_functions": sub_functions
            }
        self.__gitlab_data_producer(self.project, Core.Features.COMMITS, functions)

    ### Events ###
    def extract_events(self):
        if not self.pass_white_black_list(Core.Features.EVENTS):
            return
        self.__gitlab_data_producer(self.project, Core.Features.EVENTS, ["events", "list"])

    ### Issues ###
    def extract_issues(self):
        functions = ["issues", "list"]
        sub_functions = {}
        # ignored ["time_stats"] --> already in issue
        # ignored ["participants"] --> already in issue
        if self.pass_white_black_list(Core.Features.ISSUES_NOTES_AWARD_EMOJIS):
            if not self.use_feature_whitelist is False or Core.Features.ISSUES_NOTES not in self.feature_list:
                # If there is not a blacklist or notes are not on the blacklist then add notes award emojis.
                sub_functions[Core.Features.ISSUES_NOTES] = {
                    "attr": ["notes", "list"], 
                    "sub_functions": {Core.Features.ISSUES_NOTES_AWARD_EMOJIS: ["awardemojis", "list"]}
                }
        elif self.pass_white_black_list(Core.Features.ISSUES_NOTES):
            sub_functions[Core.Features.ISSUES_NOTES] = ["notes", "list"]
        if self.pass_white_black_list(Core.Features.ISSUES_AWARD_EMOJIS):
            sub_functions[Core.Features.ISSUES_AWARD_EMOJIS] = ["awardemojis", "list"]
        if self.pass_white_black_list(Core.Features.ISSUES_RESOURCESTATEEVENTS):
            sub_functions[Core.Features.ISSUES_RESOURCESTATEEVENTS] = ["resourcestateevents", "list"]
        if self.pass_white_black_list(Core.Features.ISSUES_RESOURCELABELEVENTS):
            sub_functions[Core.Features.ISSUES_RESOURCELABELEVENTS] = ["resourcelabelevents", "list"]
        if self.pass_white_black_list(Core.Features.ISSUES_CLOSED_BY_MR):
            sub_functions[Core.Features.ISSUES_CLOSED_BY_MR] = ["closed_by"]
        if self.pass_white_black_list(Core.Features.ISSUES_RELATED_MR):
            sub_functions[Core.Features.ISSUES_RELATED_MR] = ["related_merge_requests"]
        if self.pass_white_black_list(Core.Features.ISSUES_LINKS):
            sub_functions[Core.Features.ISSUES_LINKS] = ["links", "list"]
        if self.pass_white_black_list(Core.Features.ISSUES_RESOURCEMILESTONESEVENTS):
            sub_functions[Core.Features.ISSUES_RESOURCEMILESTONESEVENTS] = ["resourcemilestoneevents", "list"]
        if not self.pass_white_black_list(Core.Features.ISSUES):
            if not self.use_feature_whitelist:
                # If the feature is on the blacklist then ignore the feature and its subfeatures
                return
            if sub_functions == {}:
                # If the feature is not on the whitelist then ignore the feature only if no subfeature is on the whitelist
                return
        if sub_functions != {}:
            functions = {
                "attr": functions,
                "sub_functions": sub_functions
            }
        self.__gitlab_data_producer(self.project, Core.Features.ISSUES, functions)

    ### Issue boards ###
    def extract_issue_boards(self):
        functions = ["boards", "list"]
        sub_functions = {}
        if self.pass_white_black_list(Core.Features.ISSUE_BOARDS_LISTS):
            sub_functions[Core.Features.ISSUE_BOARDS_LISTS] = ["lists", "list"]
        if not self.pass_white_black_list(Core.Features.ISSUE_BOARDS):
            if not self.use_feature_whitelist:
                # If the feature is on the blacklist then ignore the feature and its subfeatures
                return
            if sub_functions == {}:
                # If the feature is not on the whitelist then ignore the feature only if no subfeature is on the whitelist
                return
        if sub_functions != {}:
            functions = {
                "attr": functions,
                "sub_functions": sub_functions
            }
        self.__gitlab_data_producer(self.project, Core.Features.ISSUE_BOARDS, functions)

    ### Labels ###
    def extract_labels(self):
        if not self.pass_white_black_list(Core.Features.LABELS):
            return
        self.__gitlab_data_producer(self.project, Core.Features.LABELS, ["labels", "list"])

    ### Merge Requests ###
    def extract_merge_requests(self):
        functions = ["mergerequests", "list"]
        sub_functions = {}
        # ignore ["pipelines", "list"] --> pipelines can be matched via commit sha
        # ignored ["time_stats"] --> already in mr
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_NOTES_AWARD_EMOJIS):
            if not self.use_feature_whitelist is False or Core.Features.MERGE_REQUESTS_NOTES not in self.feature_list:
                # If there is not a blacklist or notes are not on the blacklist then add notes award emojis.
                sub_functions[Core.Features.MERGE_REQUESTS_NOTES] = {
                    "attr": ["notes", "list"], 
                    "sub_functions": {Core.Features.MERGE_REQUESTS_NOTES_AWARD_EMOJIS: ["awardemojis", "list"]}
                }
        elif self.pass_white_black_list(Core.Features.MERGE_REQUESTS_NOTES):
            sub_functions[Core.Features.MERGE_REQUESTS_NOTES] = ["notes", "list"]
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_AWARD_EMOJIS):
            sub_functions[Core.Features.MERGE_REQUESTS_AWARD_EMOJIS] = ["awardemojis", "list"]
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_COMMITS):
            sub_functions[Core.Features.MERGE_REQUESTS_COMMITS] = ["commits"]
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_CHANGES):
            sub_functions[Core.Features.MERGE_REQUESTS_CHANGES] = ["changes"]
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_DIFFS):
            sub_functions[Core.Features.MERGE_REQUESTS_DIFFS] = ["diffs", "list"]
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_RESOURCESTATEEVENTS):
            sub_functions[Core.Features.MERGE_REQUESTS_RESOURCESTATEEVENTS] = ["resourcestateevents", "list"]
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_RESOURCELABELEVENTS):
            sub_functions[Core.Features.MERGE_REQUESTS_RESOURCELABELEVENTS] = ["resourcelabelevents", "list"]
        if self.pass_white_black_list(Core.Features.MERGE_REQUESTS_RESOURCEMILESTONESEVENTS):
            sub_functions[Core.Features.MERGE_REQUESTS_RESOURCEMILESTONESEVENTS] = ["resourcemilestoneevents", "list"]
        if not self.pass_white_black_list(Core.Features.MERGE_REQUESTS):
            if not self.use_feature_whitelist:
                # If the feature is on the blacklist then ignore the feature and its subfeatures
                return
            if sub_functions == {}:
                # If the feature is not on the whitelist then ignore the feature only if no subfeature is on the whitelist
                return
        if sub_functions != {}:
            functions = {
                "attr": functions,
                "sub_functions": sub_functions
            }
        self.__gitlab_data_producer(self.project, Core.Features.MERGE_REQUESTS, functions)
    
    ### Milestones ###
    def extract_milestones(self):
        if not self.pass_white_black_list(Core.Features.MILESTONES):
            return
        # milestone.issues() --> in issues
        # milestone.merge_requests() --> in merge requests
        self.__gitlab_data_producer(self.project, Core.Features.MILESTONES, ["milestones", "list"]  )

    ###### Pipelines and Jobs Start ######
    ### 1. Pipelines ###
    def extract_pipelines(self):
        functions = ["pipelines", "list"]
        sub_functions = {}
        if self.pass_white_black_list(Core.Features.PIPELINES_REPORT):
            sub_functions[Core.Features.PIPELINES_REPORT] = ["test_report", "get"]
        if self.pass_white_black_list(Core.Features.PIPELINES_BRIDGES):
            sub_functions[Core.Features.PIPELINES_BRIDGES] = ["bridges", "list"]
        if not self.pass_white_black_list(Core.Features.PIPELINES):
            if not self.use_feature_whitelist:
                # If the feature is on the blacklist then ignore the feature and its subfeatures
                return
            if sub_functions == {}:
                # If the feature is not on the whitelist then ignore the feature only if no subfeature is on the whitelist
                return
        if sub_functions != {}:
            functions = {
                "attr": functions,
                "sub_functions": sub_functions
            }
        self.__gitlab_data_producer(self.project, Core.Features.PIPELINES, functions)
    
    ### 2. Triggers ###
    def extract_triggers(self):
        if not self.pass_white_black_list(Core.Features.TRIGGERS):
            return
        self.__gitlab_data_producer(self.project, Core.Features.TRIGGERS, ["triggers", "list"])

    ### 3. Pipelineschedules ###
    def extract_pipelineschedules(self):
        if not self.pass_white_black_list(Core.Features.PIPELINESCHEDULES):
            return
        self.__gitlab_data_producer(self.project, Core.Features.PIPELINESCHEDULES, ["pipelineschedules", "list"])

    ### 4. Jobs ###
    def extract_jobs(self):
        if not self.pass_white_black_list(Core.Features.JOBS):
            return
        self.__gitlab_data_producer(self.project, Core.Features.JOBS, ["jobs", "list"])
    ###### Pipelines and Jobs End ######

    ### Projects ###
    def extract_project(self):
        if not self.pass_white_black_list(Core.Features.PROJECTS):
            return
        commits = self.project.commits.list(all=True)
        project_data = self.__get_gitlab_attributes(self.project.attributes)
        project_data.update({
            "contributor_count": len(self.project.repository_contributors(all=True)),
            "member_count": len(self.project.members_all.list(all=True)),
            "branch_count": len(self.project.branches.list(all=True)),
            "commit_count": len(commits),
            "last_commit_date": commits[0].attributes["created_at"],
            "labels_count": len(self.project.labels.list(all=True)),
            "milestone_count": len(self.project.milestones.list(all=True)),
            "merge_requests_count": len(self.project.mergerequests.list(all=True)),
            "release_count":  len(self.project.releases.list(all=True)),
            "issues_count": len(self.project.issues.list(all=True))
        })
        projects_df = self.get_pandas_data_frame(Core.Features.PROJECTS)
        if projects_df is None or projects_df.empty:
            self.save_as_pandas(Core.Features.PROJECTS,pd.DataFrame([project_data]))
            return
        projects_df = projects_df[projects_df.id != project_data['id']]
        projects_df = pd.concat([projects_df, pd.DataFrame([project_data])], ignore_index=True, sort=False)
        self.save_as_pandas(Core.Features.PROJECTS,projects_df)

    ### Releases ###
    def extract_releases(self):
        if not self.pass_white_black_list(Core.Features.RELEASES):
            return
        self.__gitlab_data_producer(self.project, Core.Features.RELEASES, ["releases", "list"])
        
    ### Snippets ###
    def extract_snippets(self):
        if not self.pass_white_black_list(Core.Features.SNIPPETS):
            return
        self.__gitlab_data_producer(self.project, Core.Features.SNIPPETS, ["snippets", "list"])

    ### Users ###
    def extract_users(self):
        if not self.pass_white_black_list(Core.Features.USERS):
            return
        self.__gitlab_data_producer(self.project, Core.Features.USERS, ["users", "list"])

    ### Wikis ###
    def extract_wikis(self):
        if not self.pass_white_black_list(Core.Features.WIKIS):
            return
        self.__gitlab_data_producer(self.project, Core.Features.WIKIS, ["wikis", "list"])
          
    def gitlab_data_consumer(self):
        buffer = {}
        while True:
            if not self.data_queue.empty():
                feature_name, gitlab_data = self.data_queue.get()
                if feature_name is None:
                    break
                if feature_name in buffer:
                    buffer[feature_name].append(gitlab_data)
                else:
                    buffer[feature_name] = [gitlab_data]
        
        for key, value in buffer.items():
            self.save_as_pandas(key,pd.DataFrame(value))  

    def log_serial_consumer(self):
        totals = {}
        counts = {}
        size = 60
        max_text_length = 30
        while self.consumer_thread.is_alive() or not self.log_queue.empty():
            if not self.log_queue.empty():
                feature, total = self.log_queue.get()
                if feature not in totals:
                    if totals != {}:
                        sys.stdout.write("\n")
                    totals[feature] = total
                    counts[feature] = 0
                else:
                    counts[feature] += 1
                x = int(size*counts[feature]/total)
                sys.stdout.flush()
                text = f" extracting {feature}:"
                while len(text) < max_text_length:
                    text += " "
                sys.stdout.write("%s[%s%s] %i/%i\r" % (text, "#"*x, "."*(size-x), counts[feature], total))
        sys.stdout.write("\n")
        sys.stdout.flush()
    
    def log_parallel_consumer(self):
        features = []
        sum = 0
        count = 0
        size = 60
        while self.consumer_thread.is_alive() or not self.log_queue.empty():
            if not self.log_queue.empty():
                feature, total = self.log_queue.get()
                if feature not in features:
                    features.append(feature)
                    sum += total
                else:
                    count += 1
                x = int(size*count/sum)
                sys.stdout.flush()
                sys.stdout.write("%s[%s%s] %i/%i\r" % (f" extracting parallel:         ", "#"*x, "."*(size-x), count, sum))
        sys.stdout.write("\n")
        sys.stdout.flush()

    def __gitlab_data_producer(self, gitlab_obj, feature_name:str, value, is_sub_function = False):
        if feature_name == Core.Features.ISSUES_CLOSED_BY_MR:
            x = 0
        obj = gitlab_obj
        has_sub_functions = False
        if isinstance(value, dict):
            attrs = value["attr"]
            has_sub_functions = True
        else:
            attrs = value
        for attr in attrs:
            obj = getattr(obj, attr)
        gitlab_data_list = obj(all=True)
        threads = []
        if isinstance(gitlab_data_list, dict) or hasattr(gitlab_data_list, "attributes"):
            self.producer_loop(gitlab_data_list, gitlab_obj, feature_name, value, has_sub_functions)
        else:
            if not is_sub_function and len(gitlab_data_list) > 0:
                self.log_queue.put((feature_name,len(gitlab_data_list)))
            for gitlab_data in gitlab_data_list:
                if has_sub_functions and self.extract_parallel:
                        loop_thread = threading.Thread(target=self.producer_loop, args=(gitlab_data, gitlab_obj, feature_name, value, has_sub_functions,))
                        loop_thread.start()
                        threads.append(loop_thread)
                else:
                    self.producer_loop(gitlab_data, gitlab_obj, feature_name, value, has_sub_functions)
                if not is_sub_function:
                    self.log_queue.put((feature_name,len(gitlab_data_list)))
        for thread in threads:
            thread.join()
    
    def producer_loop(self, gitlab_data, gitlab_obj, feature_name, value, has_sub_functions):
        if feature_name == Core.Features.ISSUES_CLOSED_BY_MR or feature_name == Core.Features.ISSUES_RELATED_MR:
            data = {}
            data["issue_iid"] = gitlab_obj.attributes["iid"]
            data["mr_iid"] = gitlab_data["iid"]
            data["project_id"] = gitlab_data["project_id"]
            self.data_queue.put((feature_name,data))
            return
        if feature_name == Core.Features.MERGE_REQUESTS_COMMITS:
            data = {}
            data["mr_iid"] = gitlab_obj.attributes["iid"]
            data["commit_id"] = gitlab_data["id"]
            data["project_id"] = gitlab_data["project_id"]
            self.data_queue.put((feature_name,data))
            return
        if isinstance(gitlab_data, dict):
            self.__get_gitlab_attributes(gitlab_data, feature_name, gitlab_obj.attributes["iid"])
        else:
            parent_id = None
            if feature_name == Core.Features.MERGE_REQUESTS_COMMITS:
                parent_id = gitlab_obj.attributes["iid"]
            ## ad mr changes
            self.__get_gitlab_attributes(gitlab_data.attributes, feature_name, parent_id)
            if has_sub_functions:
                for feature_name2, value2 in value["sub_functions"].items():
                    self.__gitlab_data_producer(gitlab_data,feature_name2,value2,True)

    def __get_gitlab_attributes(self, gitlab_data, feature_name = None, parent_id = None):
        data = {}
        if parent_id is not None:
            if "MRs" in feature_name:
                data["mr_iid"] = parent_id
            else:
                data["parent_id"] = parent_id
        for key, value in gitlab_data.items():
            if isinstance(value, dict):
                if key == "commit" and "id" in value:
                    data["commit_id"] = value["id"]
                elif key == "author" and "id" in value:
                    data["author_id"] = value["id"]
                elif key == "user" and "id" in value:
                    data["user_id"] = value["id"]
                elif key == "owner" and "id" in value:
                    data["owner_id"] = value["id"]
                elif key == "assignee" and "id" in value:
                    data["assignee_id"] = value["id"]
                elif key == "closed_by" and "id" in value:
                    data["closed_by_id"] = value["id"]
                elif key == "merged_by" and "id" in value:
                    # deprecated --> merge_user
                    pass
                elif key == "merge_user" and "id" in value:
                    data["merge_user_id"] = value["id"]
                elif key == "resolved_by" and "id" in value:
                    data["resolved_by_id"] = value["id"]
                elif key == "milestone" and "id" in value:
                    data["milestone_id"] = value["id"]
                elif key == "label" and "id" in value:
                    data["label_id"] = value["id"]
                elif key == "pipeline" and "id" in value:
                    data["pipeline_id"] = value["id"]
                elif key == "namespace":
                    for key2, value2 in value.items():
                        data[f"{key}_{key2}"] = value2
                else:
                    data[key] = json.dumps(value)
            elif isinstance(value, list):
                if key == "labels":
                    data[key] = value
                elif key == "assignees":
                    data["assignees_ids"] = []
                    for assignee in value:
                        data["assignees_ids"].append(assignee["id"])
                elif key == "reviewers":
                    data["reviewers_ids"] = []
                    for reviewer in value:
                        data["reviewers_ids"].append(reviewer["id"])
                elif key == "parent_ids":
                    data["parent_ids"] = []
                    for parent_id in value:
                        data["parent_ids"].append(parent_id)
                elif key == "tag_list":
                    # deprecated --> topics
                    pass
                elif key == "topics":
                    data["topics"] = []
                    for topic in value:
                        data["topics"].append(topic)
                else:
                    data[key] = json.dumps(value)
            else:
                data[key] = value
        if feature_name is None:
            return data
        self.data_queue.put((feature_name,data))

