"""Validator for commands."""
from prompt_toolkit.document import Document
from prompt_toolkit.validation import ValidationError, Validator

from .commands import COMMANDS
from .parser import parse_command


class CommandValidator(Validator):
    """Validator for commands."""

    def validate(self, document: Document) -> None:
        """
        Validate the input.

        :param document: :class:`~prompt_toolkit.document.Document` instance.
        """
        command, args = parse_command(document.text)

        if len(command) == 0:
            raise ValidationError(
                message="Enter a command, or help to list available commands!",
            )

        try:
            errors = COMMANDS[command].validate_args(command, args)
            if errors:
                raise ValidationError(
                    message="; ".join(errors),
                    cursor_position=document.cursor_position,
                )
        except KeyError:
            raise ValidationError(
                message=f"No such command {command}",
                cursor_position=document.cursor_position,
            )
