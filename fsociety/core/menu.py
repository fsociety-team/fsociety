import os.path
from colorama import Fore, Back, Style


class CommandNotFound(Exception):
    pass


class CommandCompleter(object):
    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            if text:
                self.matches = [s
                                for s in self.options
                                if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response


def set_readline(items):
    try:
        import readline
    except ImportError:
        pass
    else:
        import rlcompleter
        if isinstance(items, list):
            readline.set_completer(CommandCompleter(items).complete)
        elif isinstance(items, dict):
            readline.set_completer(CommandCompleter(items.keys()).complete)
        readline.parse_and_bind("tab: complete")


def format_menu_item(item):
    return f"{Back.WHITE}{Fore.BLACK}{item}{Style.RESET_ALL}"


def format_tools(tools):
    if isinstance(tools, dict):
        tools = tools.keys()
    return "".join([f"\n\t{str(tool)}" for tool in tools])


def module_name(module):
    return module.__name__.split(".")[-1]


def prompt(path="", base_path="~"):
    return f"\n{Fore.RED}fsociety {os.path.join(base_path, path, '')}#{Fore.WHITE} "


def confirm_install(tool_name):
    response = input(f"Do you want to install {tool_name}? (y\n): ").lower()
    if response:
        return response[0] == "y"
    return False


def tools_cli(name, tools):
    print(format_menu_item("tools") + format_tools(tools))
    set_readline(tools)
    selected_tool = input(prompt(name.split(".")[-2])).strip()
    if not selected_tool in tools.keys():
        raise CommandNotFound(selected_tool)
    tool = tools.get(selected_tool)
    tool.install()
    tool.run()
