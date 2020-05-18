import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline
from fsociety.core.config import install_dir


class s3scannerRepo(GitHubRepo):
    def __init__(self, path="sa7mon/S3Scanner", install={"pip": "requirements.txt"}):
        super().__init__(path=path, install=install)

    def run(self):
        os.chdir(self.full_path)
        set_readline([])
        user_domains = input("\nEnter one or more domains: ").strip()
        txt_path = os.path.join(install_dir, "s3_domains.txt")
        with open(txt_path, "w") as domains_file:
            for domain in user_domains.split():
                domains_file.write(domain)
        return os.system(f"python3 s3scanner.py {txt_path}")


s3scanner = s3scannerRepo()
