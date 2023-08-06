"""Command to display robot metadata."""
from abc import abstractmethod
from typing import List

from .command import BaseCommand


class MetadataCommand(BaseCommand):
    """Show all robot metadata."""

    description = "Show all robot metadata"

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        for i, v in sorted(self._tui.astoria.metadata.__dict__.items()):
            self._tui.print(f"{i}: {v}")


class GetSetMetadataCommand(BaseCommand):
    """Abstract command that gets or sets a metadata attribute."""

    @property
    @abstractmethod
    def attribute(self) -> str:
        """The atttribute of metadata to get or set."""
        raise NotImplementedError  # pragma: nocover

    async def exec(self, args: List[str]) -> None:
        """Execute the command."""
        if len(args) == 1:
            new_value = args[0]
            await self._tui.astoria.mutate_metadata(self.attribute, new_value)
        else:
            self._tui.print(
                f"{self.attribute}: "
                f"{self._tui.astoria.metadata.__dict__[self.attribute]}",
            )

    @classmethod
    def validate_args(cls, command: str, args: List[str]) -> List[str]:
        """
        Validate a list of potential arguments to the command.

        :param command: The command that has been called
        :param args: a list of arguments to validate.
        :returns: A list of errors to display.
        """
        if len(args) <= 1:
            return []
        else:
            return [f"{command} expects zero or exactly one argument."]


class ArenaCommand(GetSetMetadataCommand):
    """Get or set the arena."""

    description = "Get or set the current arena"
    attribute = "arena"


class ModeCommand(GetSetMetadataCommand):
    """Get or set the robot mode."""

    description = "Get or set the current robot mode (COMP or DEV)"
    attribute = "mode"


class ZoneCommand(GetSetMetadataCommand):
    """Get or set the zone."""

    description = "Get or set the current zone"
    attribute = "zone"
