"""Voice input layer.

This module abstracts speech capture and transcription. The runtime uses the
SpeechRecognition + PyAudio stack for live microphone capture and keeps the
API stable for future local offline expansions.
"""

from __future__ import annotations

import json
import logging
import time
from typing import Optional

logger = logging.getLogger("jarvis.core.listener")

try:
    import speech_recognition as sr
except Exception:
    sr = None


class Listener:
    """Capture voice audio and convert it to text."""

    def __init__(self) -> None:
        self.recognizer = None
        self.microphone = None
        self._warned_missing_sr = False
        self._setup()

    def _setup(self) -> None:
        """Initialize recognizer and microphone using the configured device."""
        if sr is None:
            logger.warning("SpeechRecognition dependency is not available")
            return

        try:
            self.recognizer = sr.Recognizer()
            try:
                from config import settings
                if settings.JARVIS_INPUT_DEVICE is None:
                    self.microphone = sr.Microphone()
                else:
                    self.microphone = sr.Microphone(device_index=settings.JARVIS_INPUT_DEVICE)
            except Exception:
                logger.warning("Configured input device is unavailable; retrying default microphone")
                self.microphone = sr.Microphone()

            logger.info("SpeechRecognition initialized")
        except Exception as exc:
            logger.exception("SpeechRecognition initialization failed: %s", exc)
            self.recognizer = None
            self.microphone = None

    def listen_once(self) -> Optional[str]:
        """Single-shot listen cycle for direct voice command input."""
        if sr is None or self.recognizer is None or self.microphone is None:
            if not self._warned_missing_sr:
                logger.warning("SpeechRecognition dependency is not available")
                self._warned_missing_sr = True
            return None

        for attempt in range(3):
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)

                text = self.recognizer.recognize_google(audio)
                logger.info("Recognized command: %s", text)
                return text
            except sr.WaitTimeoutError:
                logger.info("Listen timed out with no speech detected")
                return None
            except sr.UnknownValueError:
                logger.info("Could not understand audio")
                return None
            except sr.RequestError as e:
                logger.error("Could not request results from Google Speech API; %s", e)
                if attempt < 2:
                    logger.info("Retrying Google speech recognition in 1 second")
                    time.sleep(1)
                    continue
                logger.warning("Google Speech API failed after retries")
                break
            except json.JSONDecodeError as exc:
                logger.warning("Google Speech API returned malformed or empty JSON: %s", exc)
                if attempt < 2:
                    logger.info("Retrying Google speech recognition in 1 second")
                    time.sleep(1)
                    continue
                logger.warning("Google Speech API JSON decode failed after retries")
                break
            except Exception:
                logger.exception("Failed to listen")
                return None

        if hasattr(self.recognizer, "recognize_whisper"):
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)

                text = self.recognizer.recognize_whisper(audio)
                logger.info("Recognized command via local whisper fallback: %s", text)
                return text
            except Exception:
                logger.exception("Whisper fallback failed")
                return None

        logger.warning("Local whisper fallback is unavailable")
        return None

    def listen_continuous(self) -> str:
        """Placeholder for a continuous loop that can be connected to a GUI."""
        return ""
