from enum import Enum

from rich.console import Console as RichConsole
from rich.theme import Theme
from rich.traceback import install

from fsociety.core.config import get_config

config = get_config()

# Install Traceback
install()

# Console Setup
fsociety_theme = Theme(
    {
        "command": "black on white",
        "warning": "bold yellow",
        "error": "bold red",
        "info": "bold blue",
        "debug": "bright_black",
        "success": "bold green on green",
    }
)


class ConsoleLogLevel(Enum):
    DEBUG = "debug"
    INFO = "info"
    ERROR = "error"
    WARNING = "warning"


def input_wait():
    input("\nPress [ENTER] to continue... ")


class Console(RichConsole):
    """Console class for fsociety"""

    log_level: ConsoleLogLevel = ConsoleLogLevel.ERROR

    def __init__(self, log_level: ConsoleLogLevel = ConsoleLogLevel.ERROR):
        super().__init__(theme=fsociety_theme)
        self.log_level = ConsoleLogLevel(log_level)

    def set_log_level(self, level: str):
        self.log_level = ConsoleLogLevel(level)

    def debug(self, message: str, error: Exception = None, wait_input: bool = False):
        if self.log_level == ConsoleLogLevel.DEBUG:
            self.print(message, style="debug")
            if error:
                self.print_exception()
            if wait_input:
                input_wait()

    def info(self, message: str, wait_input: bool = False):
        if self.log_level in [ConsoleLogLevel.DEBUG, ConsoleLogLevel.INFO]:
            self.print(message, style="info")
            if wait_input:
                input_wait()

    def input_error(self, message: str, wait_input: bool = False):
        self.print(message, style="warning")
        if wait_input:
            input_wait()

    def error(self, message: str, wait_input: bool = False):
        self.print(message, style="error")
        if self.log_level == ConsoleLogLevel.DEBUG:
            self.print_exception()
            if wait_input:
                input_wait()

    def handle_error(self, error: Exception):
        self.error(str(error))
        if self.log_level == ConsoleLogLevel.DEBUG:
            self.print_exception()
        input_wait()

    def success(self, message: str):
        self.print(message, style="success")
        input_wait()

    def command(self, message: str):
        self.print(message, style="command")


default_log_level = config.get("fsociety", "log_level")

console = Console(ConsoleLogLevel(default_log_level))
