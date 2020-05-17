from fsociety.core.repo import GitHubRepo

install = {
    "linux": "./configure && make && make install",
    "macos": "",
    "windows": ""
}


class Repo(GitHubRepo):
    def __init__(self, name="nmap", path="nmap/nmap", install=install, default_os="linux"):
        super().__init__(name=name, path=path, install=install)

    def install(self):
        path = self.clone()


nmap = Repo()
