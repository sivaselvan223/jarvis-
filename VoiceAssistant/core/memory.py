"""Persistent assistant memory.

The memory component stores user notes, preferences, and conversation context.
The current implementation serializes a small JSON structure, allowing a later
upgrade to SQLite or a vector database.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger("jarvis.core.memory")


class Memory:
    """In-memory and on-disk user memory container."""

    def __init__(self, path: str | Path = "assets/memory.json") -> None:
        self.path = Path(path)
        self.data: Dict[str, Any] = {
            "name": "User",
            "preferences": {},
            "notes": [],
            "history": [],
        }
        self.load()

    def load(self) -> None:
        """Load memory content from disk if available."""
        try:
            if self.path.exists():
                with self.path.open("r", encoding="utf-8") as handle:
                    loaded = json.load(handle)
                    self.data.update(loaded)
                logger.info("Loaded memory from %s", self.path)
        except Exception as exc:
            logger.warning("Unable to load memory: %s", exc)

    def save(self) -> None:
        """Persist memory content."""
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8") as handle:
                json.dump(self.data, handle, indent=2)
            logger.info("Saved memory to %s", self.path)
        except Exception as exc:
            logger.exception("Unable to save memory: %s", exc)

    def remember_name(self, name: str) -> None:
        """Save the user's preferred name."""
        self.data["name"] = name
        self.save()

    def remember_preference(self, key: str, value: Any) -> None:
        """Save a preference."""
        self.data["preferences"][key] = value
        self.save()

    def add_note(self, note: str) -> None:
        """Append a note to persistent user notes."""
        self.data["notes"].append(note)
        self.save()

    def add_history(self, prompt: str, response: str) -> None:
        """Maintain a compact conversation history."""
        self.data["history"].append({"prompt": prompt, "response": response})
        self.save()
