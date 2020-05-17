# Readline Command Completer
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
        readline.set_completer(CommandCompleter(items).complete)
        readline.parse_and_bind("tab: complete")


def format_tools(tools):
    return "".join([f"\n\t{str(tool)}" for tool in tools])
