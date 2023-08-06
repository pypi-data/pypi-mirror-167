"""The quit command - exits the session."""
from typing import List

from .command import BaseCommand


class QuitCommand(BaseCommand):
    """Quit the terminal."""

    description = "Leave the terminal session."

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        self._tui.print("Goodbye!")
        self._tui.running = False
