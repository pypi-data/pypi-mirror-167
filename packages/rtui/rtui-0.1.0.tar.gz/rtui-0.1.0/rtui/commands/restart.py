"""Command to display restart running usercode."""
from typing import List

from .command import BaseCommand


class RestartUsercodeCommand(BaseCommand):
    """Restart running usercode."""

    description = "Restart running code"

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        await self._tui.astoria.restart_usercode()
