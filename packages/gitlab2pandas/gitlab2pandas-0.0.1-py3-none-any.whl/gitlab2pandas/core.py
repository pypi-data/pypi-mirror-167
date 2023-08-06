from pathlib import Path
import pickle
import pandas as pd
import os

class Core():
    class Features():
        # Name <= 31 chars
        USERS = "Users"
        BRANCHES = "Branches"
        RELEASES = "Releases"
        PIPELINES = "Pipelines"
        PIPELINES_REPORT = "PipelinesReport"
        PIPELINES_BRIDGES = "PipelinesBridges"
        JOBS = "Jobs"
        ISSUES = "Issues"
        ISSUES_NOTES = "IssuesNotes"
        ISSUES_AWARD_EMOJIS = "IssuesAwardEmojis"
        ISSUES_NOTES_AWARD_EMOJIS = "IssuesNotesAwardEmojis"
        ISSUES_RESOURCESTATEEVENTS = "IssuesResourcestateevents"
        ISSUES_RESOURCELABELEVENTS = "IssuesResourcelabelevents"
        ISSUES_RESOURCEMILESTONESEVENTS = "IssuesResourcemilestonesevents"
        ISSUES_CLOSED_BY_MR = "IssuesClosedByMR"
        ISSUES_RELATED_MR = "IssuesRelatedMR"
        ISSUES_LINKS = "IssuesLinks"
        MERGE_REQUESTS = "MergeRequests"
        MERGE_REQUESTS_NOTES = "MRsNotes"
        MERGE_REQUESTS_COMMITS = "MRsCommits"
        MERGE_REQUESTS_AWARD_EMOJIS = "MRsAwardEmojis"
        MERGE_REQUESTS_NOTES_AWARD_EMOJIS = "MRsNotesAwardEmojis"
        MERGE_REQUESTS_RESOURCESTATEEVENTS = "MRsResourcestateevents"
        MERGE_REQUESTS_RESOURCELABELEVENTS = "MRsResourcelabelevents"
        MERGE_REQUESTS_CHANGES = "MRsChanges"
        MERGE_REQUESTS_DIFFS = "MRsDiffs"
        MERGE_REQUESTS_RESOURCEMILESTONESEVENTS = "MRsResourcemilestonesevents"
        COMMITS = "Commits"
        COMMITS_COMMENTS = "CommitsComments"
        COMMITS_REFS = "CommitsRefs"
        COMMITS_DIFFS = "CommitsDiffs"
        COMMITS_STATUSES = "CommitStatuses"
        PROJECTS = "Projects"
        EVENTS = "Events"
        ISSUE_BOARDS = "IssueBoards"
        ISSUE_BOARDS_LISTS = "IssueBoardsLists"
        LABELS = "Labels"
        TRIGGERS = "Triggers"
        PIPELINESCHEDULES = "Pipelineschedules"
        RUNNERS = "Runners"
        RUNNERS_JOBS = "RunnersJobs"
        SNIPPETS = "Snippets"
        WIKIS = "Wikis"
        MILESTONES = "Milestones"

        @classmethod
        def to_list(cls) -> list:
            features = []
            for var, value in vars(cls).items():
                if isinstance(value,str):
                    if not var.startswith("__"):
                        features.append(value)
            return features

    def __init__(self, data_root_dir:str, project = None, project_namespace = None, project_name = None) -> None:
        self.data_root_dir = data_root_dir
        self.project = project
        self.project_namespace = project_namespace
        self.project_name = project_name
        if project is None and (project_namespace is None or project_name is None):
            raise Exception("Need a project or its namespace and name")
        if project is None:
            self.repo_data_dir = Path(self.data_root_dir,project_namespace,project_name)
        else:
            self.repo_data_dir = Path(self.data_root_dir,project.attributes["path_with_namespace"])
            self.repo_data_dir.mkdir(parents=True, exist_ok=True)

    def save_as_pandas(self, filename:str, data:pd.DataFrame):
        if filename == Core.Features.PROJECTS:
            pd_file = Path(self.data_root_dir, f"{filename}.p")
        else:
            pd_file = Path(self.repo_data_dir, f"{filename}.p")
        with open(pd_file, "wb") as f:
            pickle.dump(data, f)
    
    def get_pandas_data_frame(self, filename:str) -> pd.DataFrame:
        if filename == Core.Features.PROJECTS:
            pd_file = Path(self.data_root_dir, f"{filename}.p")
        else:
            pd_file = Path(self.repo_data_dir, f"{filename}.p")
        if pd_file.is_file():
            return pd.read_pickle(pd_file)
        else:
            return None
              
    def convert_to_excel(self, excel_filename):
        writer = pd.ExcelWriter(Path(self.repo_data_dir, f'{excel_filename}.xlsx'), engine='xlsxwriter')
        for feature in Core.Features.to_list():
            df = self.get_pandas_data_frame(feature)
            if df is not None:
                df.to_excel(writer, sheet_name=feature)
        writer.close()