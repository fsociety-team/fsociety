import os

from fsociety.core.repo import GitHubRepo
from fsociety.core.menu import set_readline, confirm


class gitgraberRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="hisxo/gitGraber",
                         install={"pip": "requirements.txt"},
                         description="Search and find sensitive data in real time for GitHub")

    def run(self):
        os.chdir(self.full_path)
        wordlists_path = os.path.join(self.full_path, "wordlists")
        set_readline([])
        user_query = input("\nEnter a search query: ").strip()
        set_readline([f for f in os.listdir(os.path.join(self.full_path, "wordlists"))
                      if os.path.isfile(os.path.join(os.path.join(self.full_path, "wordlists"), f))])
        user_keywords = input(
            "\nEnter a keywords path [default=keywords.txt]: ").strip()
        if not user_keywords:
            user_keywords = "keywords.txt"
        keywords_path = os.path.join(wordlists_path, user_keywords)
        if confirm("\nDo you want to add a GitHub token?"):
            github_token = input(
                "\nEnter a GitHub token: ").strip() 
            os.environ["GITHUB_TOKENS"] = f"['{github_token}']"
        return os.system(f"python3 gitGraber.py -k {keywords_path} -q {user_query}")


gitgraber = gitgraberRepo()
