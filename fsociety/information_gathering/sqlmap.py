import os

from fsociety.core.menu import confirm
from fsociety.core.repo import GitHubRepo


class SqlmapRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="sqlmapproject/sqlmap",
            install=None,
            description="Automatic SQL injection and database takeover tool",
        )

    def run(self):
        os.chdir(self.full_path)
        user_url = input("\nEnter a url to scan: ").strip()
        user_args = str()
        if confirm("\nDo you want to add any extra args?"):
            os.system("python3 sqlmap.py --help")
            user_args = input("\nEnter any extra args: ").strip()
        return os.system(f"python3 sqlmap.py -u {user_url} {user_args}")


sqlmap = SqlmapRepo()
