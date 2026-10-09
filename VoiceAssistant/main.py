"""Main entry point for the Jarvis-style Python voice assistant.

This file wires the major runtime components together:
- the speech listener
- the speech speaker
- the command router
- the wake word detector
- the assistant orchestration layer

The system is intentionally designed to support offline recognition and
fallback reasoning through an OpenAI-compatible API, with optional cloud voice
synthesis through ElevenLabs.
"""

from __future__ import annotations

import asyncio
import logging
import os
import sys
from pathlib import Path

from config import settings
from core.assistant import Assistant
from core.listener import Listener
from core.speaker import Speaker
from core.command_router import CommandRouter
from core.wake_word import WakeWordListener


logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL, logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("jarvis.main")


class JarvisApp:
    """Composition root for the voice assistant application."""

    def __init__(self) -> None:
        self.config = settings
        self.speaker = Speaker()
        self.listener = Listener()
        self.router = CommandRouter()
        self.assistant = Assistant(self.listener, self.speaker, self.router)
        self.wake_word = WakeWordListener(self.assistant)

    async def start(self) -> None:
        """Start the assistant runtime asynchronously."""
        logger.info("Starting Jarvis Assistant")
        self.speaker.speak("Jarvis systems online")
        await self.assistant.run()

    def run(self) -> None:
        """Synchronous wrapper for async runtime."""
        try:
            asyncio.run(self.start())
        except KeyboardInterrupt:
            logger.info("Shutdown requested by user")
            self.speaker.speak("Shutting down")
            sys.exit(0)
        except Exception as exc:
            logger.exception("Runtime failure: %s", exc)
            self.speaker.speak("A system error occurred")
            sys.exit(1)


if __name__ == "__main__":
    app = JarvisApp()
    app.run()
