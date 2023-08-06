"""The TUI class."""

import asyncio

from prompt_toolkit import PromptSession, print_formatted_text

from rtui.astoria import AstoriaIntegration

from .commands import COMMANDS
from .parser import parse_command
from .validator import CommandValidator


class TUI:
    """The Terminal User Interface."""

    def __init__(self) -> None:
        self._session = self._get_session()
        self.running: bool = True
        self.commands = COMMANDS

        self.astoria = AstoriaIntegration(False, None)

    def _get_session(self) -> PromptSession[str]:
        """Get a prompt session."""
        return PromptSession(
            message="> ",
            validator=CommandValidator(),
            validate_while_typing=False,
        )

    def print(self, text: str) -> None:
        """
        Print something to the terminal.

        This is a convenience alias for print_formatted_text.
        """
        print_formatted_text(text)

    async def run_tui(self) -> None:
        """Run the main loop for the TUI."""
        asyncio.create_task(self.astoria.run())
        await self.welcome()
        try:
            while self.running:
                command = await self._session.prompt_async()
                if command:
                    await self.exec_command(command)
        except EOFError:
            pass

    async def exec_command(self, input: str) -> None:
        """
        Execute a command.

        :param input: The full command to execute.
        """
        command, args = parse_command(input)
        try:
            com_class = self.commands[command]
            com = com_class(self)
            await com.exec(args)
        except KeyError:
            # Note: this is theoretically unreachable, as we validate that commands exist
            self.print(f"Unknown command: {command}")  # pragma: nocover

    async def welcome(self) -> None:
        """Print the welcome message."""
        self.print("Student Robotics OS\n")
        await self.exec_command("help")
        self.print("")
