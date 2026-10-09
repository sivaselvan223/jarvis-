"""Configuration settings for the Jarvis-style voice assistant.

This module centralizes environment-dependent behavior. The assistant can use
OpenAI-compatible APIs for language reasoning and ElevenLabs for cloud speech.

The implementation intentionally keeps values explicit and small enough to be
understood and extended for a real Windows desktop environment.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Application-level configuration values."""

    APP_NAME: str = "Jarvis Assistant"
    APP_VERSION: str = "0.1.0"

    # Runtime behavior
    LOG_LEVEL: str = "INFO"
    OFFLINE_MODE: bool = True
    WAKE_WORD: str = "jarvis"
    ENABLE_WAKE_WORD: bool = True
    ENABLE_CONTINUOUS_LISTENING: bool = True

    # Audio and speech
    DEFAULT_VOICE_RATE: int = 150
    DEFAULT_VOLUME: float = 1.0
    SPEECH_ENGINE: str = "pyttsx3"
    JARVIS_INPUT_DEVICE: int = 1

    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent
    LOGS_DIR: Path = BASE_DIR / "logs"
    ASSETS_DIR: Path = BASE_DIR / "assets"
    MEMORY_PATH: Path = BASE_DIR / "assets" / "memory.json"

    # AI services
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"
    ELEVENLABS_API_KEY: str = ""
    ELEVENLABS_VOICE_ID: str = ""

    # Speech recognition
    WHISPER_MODEL: str = "base"
    WHISPER_DEVICE: str = "cpu"

    # GUI
    GUI_THEME: str = "dark"
    UI_WIDTH: int = 1100
    UI_HEIGHT: int = 720

    # System integration toggles
    ENABLE_SYSTEM_COMMANDS: bool = True
    ENABLE_BROWSER_COMMANDS: bool = True
    ENABLE_MEDIA_COMMANDS: bool = True


settings = Settings()

# Optional environment-based override points.
def _env_int(name: str, fallback: int) -> int:
    raw_value = os.getenv(name)
    if raw_value is None:
        return fallback
    try:
        return int(raw_value)
    except (TypeError, ValueError):
        return fallback

settings = Settings(
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", settings.OPENAI_API_KEY),
    OPENAI_BASE_URL=os.getenv("OPENAI_BASE_URL", settings.OPENAI_BASE_URL),
    ELEVENLABS_API_KEY=os.getenv("ELEVENLABS_API_KEY", settings.ELEVENLABS_API_KEY),
    ELEVENLABS_VOICE_ID=os.getenv("ELEVENLABS_VOICE_ID", settings.ELEVENLABS_VOICE_ID),
    JARVIS_INPUT_DEVICE=_env_int("JARVIS_INPUT_DEVICE", settings.JARVIS_INPUT_DEVICE),
    LOG_LEVEL=os.getenv("JARVIS_LOG_LEVEL", settings.LOG_LEVEL),
    OFFLINE_MODE=os.getenv("JARVIS_OFFLINE_MODE", "true").lower() in {"1", "true", "yes", "on"},
)
