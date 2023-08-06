from pathlib import Path
import threading
import pandas as pd
from gitlab2pandas.core import Core
from gitlab2pandas.extractions import Extractions
from gitlab import Gitlab

class GitLab2Pandas(Core):

    def extract_all(self, extract_parallel = False, feature_blacklist = [], feature_whitelist = []):
        # parallel extraction might fail for some repositories because of server settings

        extractions = Extractions(self.data_root_dir, project=self.project, extract_parallel=extract_parallel)
        extractions.start(feature_blacklist, feature_whitelist)

        
    @staticmethod
    def get_project(server_url, project_namespace, project_name, private_token=None, oauth_token=None, job_token=None):
        gl = None
        if private_token:
            # private token or personal token authentication
            gl = Gitlab(server_url, private_token=private_token, per_page=100)
        elif oauth_token:
            # oauth token authentication
            gl = Gitlab(server_url, oauth_token=oauth_token, per_page=100)
        elif job_token:
            # job token authentication (to be used in CI)
            gl = Gitlab(server_url, job_token=job_token, per_page=100)
        else:
            # anonymous gitlab instance, read-only for public resources
            gl = Gitlab(server_url)
        return gl.projects.get(f"{project_namespace}/{project_name}", per_page=100)