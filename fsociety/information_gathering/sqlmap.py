import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import confirm


class sqlmapRepo(GitHubRepo):
    def __init__(self, path="sqlmapproject/sqlmap", install=None):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        user_url = input("\nEnter a url to scan: ").strip()
        args = str()
        if confirm("Do you want to add any extra args?"):
            os.system(f"python3 sqlmap.py --help")
            user_args = input("\nEnter any extra args: ").strip()
        return os.system(f"python3 sqlmap.py -u {user_url} {user_args}")


sqlmap = sqlmapRepo()
