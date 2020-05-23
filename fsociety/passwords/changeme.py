import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline
from fsociety.core.hosts import get_hosts, add_host, InvalidHost


class changemeRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="ztgrace/changeme",
                         install={"pip": "requirements.txt"},
                         description="A default credential scanner")

    def run(self):
        os.chdir(self.full_path)
        hosts = get_hosts()
        set_readline(hosts)
        user_host = input("\nEnter a host: ").strip()
        return os.system(f"python3 changeme.py {user_host}")


changeme = changemeRepo()
