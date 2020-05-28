# Core
from fsociety.core.menu import tools_cli

from .sqlmap import sqlmap
from .sublist3r import sublist3r
from .sherlock import sherlock
from .s3scanner import s3scanner
from .gitgraber import gitgraber

__tools__ = [sqlmap, sublist3r, sherlock, s3scanner, gitgraber]


def cli():
    tools_cli(__name__, __tools__)
