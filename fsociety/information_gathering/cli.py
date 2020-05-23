# Core
from fsociety.core.menu import tools_cli

from .nmap import nmap
from .sqlmap import sqlmap
from .sublist3r import sublist3r
from .sherlock import sherlock
from .s3scanner import s3scanner

__tools__ = [nmap, sqlmap, sublist3r, sherlock, s3scanner]


def cli():
    tools_cli(__name__, __tools__)
