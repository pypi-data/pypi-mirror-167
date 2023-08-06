"""Base Command classes."""
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from rtui.tui import TUI


class BaseCommand(metaclass=ABCMeta):
    """A base command class."""

    def __init__(self, tui: 'TUI') -> None:
        self._tui = tui

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Description of the command.

        Displayed as a single line in the help text.

        :returns: Description of the command.
        """
        raise NotImplementedError  # pragma: nocover

    @abstractmethod
    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        raise NotImplementedError  # pragma: nocover

    @classmethod
    def validate_args(cls, command: str, args: List[str]) -> List[str]:
        """
        Validate a list of potential arguments to the command.

        :param command: The command that has been called
        :param args: a list of arguments to validate.
        :returns: A list of errors to display.
        """
        if len(args) == 0:
            return []
        else:
            return [f"{command} does not expect any arguments."]
