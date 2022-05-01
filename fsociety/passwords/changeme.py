import os

from fsociety.core.hosts import InvalidHost, add_host, get_hosts
from fsociety.core.menu import set_readline
from fsociety.core.repo import GitHubRepo


class ChangemeRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="ztgrace/changeme",
            install={"pip": "requirements.txt"},
            description="A default credential scanner",
        )

    def run(self):
        os.chdir(self.full_path)
        hosts = get_hosts()
        set_readline(hosts)
        user_host = input("\nEnter a host: ").strip()
        if not user_host:
            raise InvalidHost
        if user_host not in hosts:
            add_host(user_host)
        return os.system(f"python3 changeme.py {user_host}")


changeme = ChangemeRepo()
