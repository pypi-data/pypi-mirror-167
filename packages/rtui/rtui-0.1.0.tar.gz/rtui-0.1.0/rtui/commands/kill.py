"""Command to display kill running usercode."""
from typing import List

from .command import BaseCommand


class KillUsercodeCommand(BaseCommand):
    """Kill running usercode."""

    description = "Kill running code"

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        await self._tui.astoria.kill_usercode()
