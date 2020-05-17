# Core
from fsociety.core.menu import set_readline, format_tools

from .nmap import nmap

__tools__ = [nmap]


def cli():
    print("Information Gathering!")
    print(format_tools(__tools__))
    set_readline(__tools__)
    selected_tool = input("Select a tool: ")
    print(selected_tool)
