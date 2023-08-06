"""The help command - print available commands."""
from typing import List

from .command import BaseCommand


class HelpCommand(BaseCommand):
    """Show the available commands.."""

    description = "Show available commands"

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        if len(args) == 0 or args[0] not in self._tui.commands:
            self._tui.print("Available commands:")
            for command, com_class in self._tui.commands.items():
                print(f"{command}: {com_class.description}")
        else:
            try:
                com_class = self._tui.commands[args[0]]
                print(f"{args[0]}: {com_class.description}")
            except KeyError:
                self._tui.print(f"Unknown command: {args[0]}")

    @classmethod
    def validate_args(cls, command: str, args: List[str]) -> List[str]:
        """
        Validate a list of potential arguments to the command.

        :param command: The command that has been called
        :param args: a list of arguments to validate.
        :returns: A list of errors to display.
        """
        if len(args) < 2:
            return []
        else:
            return [f"{command} takes either none or exactly one argument."]
