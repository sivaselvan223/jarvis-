"""High-level orchestration layer.

The assistant coordinates wake detection, listening, command execution,
memory, AI chat, and response generation.
"""

from __future__ import annotations

import asyncio
import logging
import random

from core.memory import Memory
from core.command_router import CommandRouter
from core.listener import Listener
from core.speaker import Speaker

logger = logging.getLogger("jarvis.core.assistant")


SUCCESS_RESPONSES = [
    "Done, Sir.",
    "Task completed successfully.",
    "Completed.",
    "Operation completed.",
    "Finished.",
    "Your request has been completed.",
    "Everything is ready.",
    "Done. Anything else?"
]


class Assistant:
    """Main conversational and command execution engine."""

    def __init__(
        self,
        listener: Listener,
        speaker: Speaker,
        router: CommandRouter,
    ) -> None:

        self.listener = listener
        self.speaker = speaker
        self.router = router
        self.memory = Memory()

        self.is_listening = False

    async def run(self) -> None:
        """Main assistant loop."""

        logger.info("Assistant runtime loop started")

        self.is_listening = True

        while self.is_listening:

            try:
                command = self.listener.listen_once()

                if not command:
                    continue

                response = await self.process_command(command)

                if response:
                    self.speaker.speak(response)

            except asyncio.CancelledError:
                logger.info("Assistant loop cancelled")
                break

            except Exception as exc:
                logger.exception("Assistant runtime error: %s", exc)
                self.speaker.speak("Sorry Sir, I encountered an unexpected error.")

    async def process_command(self, text: str) -> str:
        """Process a spoken command."""

        command = text.strip()

        logger.info("Processing command: %s", command)

        if not command:
            return "I did not hear a command."

        command = command.lower()

        # Remove wake word
        if "jarvis" in command:
            command = command.replace("jarvis", "").strip()

        if command == "":
            return "Yes Sir, I am listening."

        try:
            logger.info("Executing command: %s", command)

            result = await self.router.route(command)

            if result:

                result = result.strip()

                # If the command already returns a natural response,
                # don't add another prefix.
                if result.lower().startswith((
                    "opening",
                    "launching",
                    "playing",
                    "searching",
                    "turning",
                    "taking",
                    "saving",
                    "creating",
                    "deleting",
                    "sending",
                    "opening weather",
                    "done",
                    "completed",
                )):
                    return result

                return f"{random.choice(SUCCESS_RESPONSES)} {result}"

            return random.choice(SUCCESS_RESPONSES)

        except Exception as exc:
            logger.exception("Command execution failed: %s", exc)
            return "Sorry Sir, I couldn't complete that task."

    async def respond(self, prompt: str) -> str:
        """Fallback conversational response."""
        return f"I am thinking about {prompt}"