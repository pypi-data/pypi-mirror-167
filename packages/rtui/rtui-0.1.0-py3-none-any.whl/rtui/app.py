"""Application entrypoint."""

import asyncio

from .tui import TUI

loop = asyncio.get_event_loop()


def app() -> None:
    """The entrypoint to the TUI."""
    tui = TUI()

    loop.run_until_complete(tui.run_tui())
