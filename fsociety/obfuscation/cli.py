# Core
from fsociety.core.menu import tools_cli

from .cuteit import cuteit
from .zhesp2 import zhesp2

__tools__ = [cuteit, zhesp2]


def cli():
    tools_cli(__name__, __tools__)
