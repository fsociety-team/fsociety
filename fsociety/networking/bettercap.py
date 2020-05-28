import os
from shutil import which

from fsociety.core.repo import GitHubRepo


class bettercapRepo(GitHubRepo):
    def __init__(self):
        super().__init__(path="bettercap/bettercap",
                         install={
                             "linux": "sudo apt install golang git build-essential libpcap-dev libusb-1.0-0-dev libnetfilter-queue-dev; go get -u github.com/bettercap/bettercap",
                             "brew": "install bettercap"
                         },
                         description="Swiss army knife for network attacks and monitoring")

    def installed(self):
        return which("bettercap")

    def install(self):
        super().install(clone=False)

    def run(self):
        print("Please note that bettercap must be run with sudo")
        return os.system("sudo bettercap")


bettercap = bettercapRepo()
