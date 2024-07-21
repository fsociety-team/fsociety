from typing import Optional, Union

from rich.style import Style

from fsociety.console import console
from fsociety.core.config import get_config

# Config
config = get_config()


def input_wait():
    input("\nPress [ENTER] to continue... ")


def errorhandle(error: Exception, style: Optional[Union[str, Style]] = "red") -> None:
    console.print(str(error), style=style)
    if config.get("fsociety", "log_level") == "debug":
        console.print_exception()
    input_wait()
    return


def doexcept(error: Exception, style: Optional[Union[str, Style]] = "red") -> None:
    try:
        raise error
    except Exception as e:
        errorhandle(e, style=style)
