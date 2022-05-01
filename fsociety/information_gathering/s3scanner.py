import os

from fsociety.core.config import INSTALL_DIR
from fsociety.core.menu import set_readline
from fsociety.core.repo import GitHubRepo


class S3scannerRepo(GitHubRepo):
    def __init__(self):
        super().__init__(
            path="sa7mon/S3Scanner",
            install={"pip": "requirements.txt"},
            description="A tool to find open S3 buckets and dump their contents",
        )

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_domains = input("\nEnter one or more domains: ").strip()
        txt_path = os.path.join(INSTALL_DIR, "s3_domains.txt")
        with open(txt_path, "w") as domains_file:
            for domain in user_domains.split():
                domains_file.write(domain)
        return os.system(f"python3 s3scanner.py {txt_path}")


s3scanner = S3scannerRepo()
