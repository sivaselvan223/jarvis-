"""Wake-word listener and runtime trigger.

The assistant is designed to respond to "Jarvis" as a hotword. The default
implementation uses optional keyboard and system hooks, and can be connected to
SpeechRecognition or a custom microphone listener.
"""

from __future__ import annotations

import logging

logger = logging.getLogger("jarvis.core.wake_word")

try:
    import keyboard
except Exception:
    keyboard = None


class WakeWordListener:
    """Simple wake-word bridge for continuous monitoring."""

    def __init__(self, assistant) -> None:
        self.assistant = assistant
        self.enabled = True

    def start(self) -> None:
        """Start wake-word monitoring loop."""
        logger.info("Wake-word listener started")

    def stop(self) -> None:
        """Stop wake-word monitoring."""
        logger.info("Wake-word listener stopped")

    def detect(self, text: str) -> bool:
        """Check whether the spoken text includes the configured wake word."""
        return "jarvis" in text.lower()
