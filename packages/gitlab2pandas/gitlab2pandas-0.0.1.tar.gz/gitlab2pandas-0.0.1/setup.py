# use pipenv-setup to generate the requirement list
# https://pypi.org/project/pipenv-setup/

from setuptools import setup
from gitlab2pandas import __version__


with open("README.md", "r") as f:
   long_description = f.read()



setup(
   name="gitlab2pandas",
   version=__version__,
   packages=["gitlab2pandas"],
   license="BSD 2",
   description="gitlab2pandas supports the aggregation of project activities in a GitLab repository and makes them available in pandas dataframes",
   long_description = long_description,
   long_description_content_type="text/markdown",
   author="Maximilian Karl",
   url="",
   download_url=f"",
   keywords=["git", "gitlab", "collaborative code development", "git mining"],
   install_requires=[
   ], 
   classifiers=[
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
   ],
   python_requires=">=3.8"
)
