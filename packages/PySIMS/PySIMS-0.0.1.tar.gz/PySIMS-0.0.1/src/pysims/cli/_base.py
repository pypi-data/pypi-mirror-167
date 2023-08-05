r"""The _display module contains functions and configuration for displaying output to the user in the terminal."""

# Standard Library
from enum import Enum
from typing import Optional

# Third Party
import click

# Local


class Colors(Enum):
    r"""Colors used for terminal output."""
    GREEN = 'green'
    RED = 'red'
    YELLOW = 'yellow'


def exit_program(ctx: click.Context, error: bool, message: Optional[str]) -> None:
    """Exit the program with an exit code and optional message.

    Parameters
    ----------
    ctx : click.core.Context
        The context of the program.

    error : bool
        True if an error occurred and False otherwise.
        - exit_code = 0: Success
        - exit_code = 1: Error

    message: str or None, default None
        An optional message to print before exiting.
        If None no message is printed.
    """

    if error:
        exit_code = 1
        color = Colors.RED
    else:
        exit_code = 0
        color = None

    click.secho(message=message, fg=color.value)
    ctx.exit(code=exit_code)
