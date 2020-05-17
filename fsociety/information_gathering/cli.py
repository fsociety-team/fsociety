# Core
from fsociety.core.menu import tools_cli

from .nmap import nmap

__tools__ = {
    "nmap": nmap
}


def cli():
    tools_cli(__name__, __tools__)
