# Core
from fsociety.core.menu import tools_cli

from .nmap import nmap
from .sherlock import sherlock

__tools__ = {
    "nmap": nmap,
    "sherlock": sherlock,
}


def cli():
    tools_cli(__name__, __tools__)
