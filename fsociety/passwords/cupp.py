import os

from fsociety.core.repo import GitHubRepo


class cuppRepo(GitHubRepo):
    def __init__(self, path="Mebus/cupp", install=None):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        return os.system("python3 cupp.py -i")


cupp = cuppRepo()
