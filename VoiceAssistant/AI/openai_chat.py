"""Optional OpenAI-compatible chat adapter.

The runtime does not require this file to exist at import time, but it keeps
one consistent LLM adapter surface for future cloud integration.
"""

from __future__ import annotations

import logging
import os

logger = logging.getLogger("jarvis.ai.openai")

try:
    import openai
except Exception:
    openai = None


class OpenAIChat:
    """Thin OpenAI-style API adapter."""

    def __init__(self, api_key: str = "", model: str = "gpt-4o-mini") -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY", "")
        self.model = model

    def ask(self, prompt: str) -> str:
        """Query an OpenAI-compatible model when API configuration is present."""
        if openai is None or not self.api_key:
            return "OpenAI integration is not configured"

        try:
            client = openai.OpenAI(api_key=self.api_key)
            completion = client.responses.create(
                model=self.model,
                input=prompt,
            )
            return str(completion.output_text)
        except Exception as exc:
            logger.warning("OpenAI request failed: %s", exc)
            return "The cloud AI service is not available"
