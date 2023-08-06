"""RTUI Astoria Integration."""

from json import JSONDecodeError, loads
from typing import Match, Optional

from astoria.common.components import StateConsumer
from astoria.common.config import AstoriaConfig
from astoria.common.ipc import (
    ManagerRequest,
    MetadataManagerMessage,
    MetadataSetManagerRequest,
    UsercodeLogBroadcastEvent,
)
from astoria.common.metadata import Metadata
from prompt_toolkit import print_formatted_text
from pydantic import ValidationError, parse_obj_as


class AstoriaIntegration(StateConsumer):
    """Astoria Consumer for RTUI."""

    name = "rtui"

    dependencies = ["astprocd", "astdiskd", "astmetad"]

    def __init__(self, verbose: bool, config_file: Optional[str]) -> None:
        self.config = AstoriaConfig.load(config_file)

        self._setup_logging(verbose, welcome_message=False)
        self._setup_event_loop()
        self._setup_mqtt()

        self._init()

    def _init(self) -> None:
        # State Manager Messages
        self._mqtt.subscribe("astmetad", self.handle_astmetad_message)

        # Broadcasts
        self._mqtt.subscribe("broadcast/usercode_log", self.handle_log)

        self.metadata: Optional[Metadata] = None

    async def main(self) -> None:
        """Main method of the data component."""
        await self.wait_loop()

    async def handle_astmetad_message(
            self,
            match: Match[str],
            payload: str,
    ) -> None:
        """Event handler for metadata changes."""
        if payload:
            try:
                metadata_manager_message = parse_obj_as(
                    MetadataManagerMessage,
                    loads(payload),
                )
                self.metadata = metadata_manager_message.metadata
            except (ValidationError, JSONDecodeError):
                print_formatted_text("Bad Message from astmetad")
        else:
            print_formatted_text("Bad Message from astmetad")

    async def handle_log(
            self,
            match: Match[str],
            payload: str,
    ) -> None:
        """Event handler for metadata changes."""
        if payload:
            try:
                log_event = parse_obj_as(UsercodeLogBroadcastEvent, loads(payload))
                print_formatted_text(log_event.content, end="")
            except (ValidationError, JSONDecodeError):
                print_formatted_text("Bad log event")
        else:
            print_formatted_text("Bad log event")

    async def kill_usercode(self) -> None:
        """Kill running usercode."""
        res = await self._mqtt.manager_request(
            "astprocd",
            "kill",
            ManagerRequest(sender_name=self.name),
        )
        if res.success:
            print_formatted_text("Successfully killed code.")
            if len(res.reason) > 0:
                print_formatted_text(res.reason)
        else:
            print_formatted_text("Unable to kill code.")
            if len(res.reason) > 0:
                print_formatted_text(res.reason)

    async def restart_usercode(self) -> None:
        """Restart running usercode."""
        res = await self._mqtt.manager_request(
            "astprocd",
            "restart",
            ManagerRequest(sender_name=self.name),
        )
        if res.success:
            print_formatted_text("Successfully restarted code.")
            if len(res.reason) > 0:
                print_formatted_text(res.reason)
        else:
            print_formatted_text("Unable to restart code.")
            if len(res.reason) > 0:
                print_formatted_text(res.reason)

    async def mutate_metadata(self, attr: str, value: str) -> None:
        """
        Mutate the metadata.

        :param attr: The attribute to mutate.
        :param value: The value to change the attribute to.
        """
        res = await self._mqtt.manager_request(
            "astmetad",
            "mutate",
            MetadataSetManagerRequest(
                sender_name=self.name,
                attr=attr,
                value=value,
            ),
        )
        if res.success:
            print_formatted_text(f"Successfully set {attr} to {value}.")
            if len(res.reason) > 0:
                print_formatted_text(res.reason)
        else:
            print_formatted_text(f"Unable to set {attr} to {value}.")
            if len(res.reason) > 0:
                print_formatted_text(res.reason)
