# Core
from fsociety.core.menu import tools_cli

from .xsstrike import xsstrike
from .photon import photon

__tools__ = [xsstrike, photon]


def cli():
    tools_cli(__name__, __tools__)
