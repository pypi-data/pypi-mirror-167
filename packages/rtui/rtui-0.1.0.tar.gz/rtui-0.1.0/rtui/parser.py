"""Helper functions for parsing commands."""
import re
from typing import List, Tuple


def parse_command(input: str) -> Tuple[str, List[str]]:
    """
    Parse the command.

    :param input: The input to parse.
    :returns: Tuple of command, and a list of parameters to the command.
    """
    input = input.strip()  # Strip whitespace at start and end.
    input = re.sub(r"\s\s+", " ", input)  # Remove double spaces.
    tokens = input.split(" ")
    command = tokens.pop(0)
    return command, tokens
