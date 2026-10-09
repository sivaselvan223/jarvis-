"""Voice output layer.

This module speaks responses back to the user using the configured local
speech engine. The runtime is offline-first and uses pyttsx3 for Windows text
output. OpenAI and cloud voice services are optional and disabled by default.
"""

from __future__ import annotations

import logging

logger = logging.getLogger("jarvis.core.speaker")

try:
    import pyttsx3
except Exception:
    pyttsx3 = None

from config import settings


class Speaker:
    """Speech synthesis support backed by pyttsx3."""

    def __init__(self) -> None:
        self.engine = None
        self.tts_mode = "offline"
        self._setup()

    def _setup(self) -> None:
        """Create and configure the speech engine."""
        if settings.OFFLINE_MODE:
            self.tts_mode = "offline"
        elif pyttsx3 is not None:
            self.tts_mode = "offline"

        if pyttsx3 is None:
            logger.warning("pyttsx3 is not installed; speech synthesis disabled")
            return

        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", settings.DEFAULT_VOICE_RATE)
            logger.info("pyttsx3 initialized")
        except Exception as exc:
            logger.exception("pyttsx3 initialization failed: %s", exc)

    def speak(self, text: str) -> None:
        """Speak a response string if the engine is available."""
        if not text:
            return

        logger.info("Speaking: %s", text)
        if self.engine is None:
            logger.warning("No TTS engine available; cannot speak")
            return

        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as exc:
            logger.exception("Speech output error: %s", exc)

    def stop(self) -> None:
        """Stop current playback."""
        if self.engine is not None:
            try:
                self.engine.stop()
            except Exception as exc:
                logger.exception("Stop error: %s", exc)
