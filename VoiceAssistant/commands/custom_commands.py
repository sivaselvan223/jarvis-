"""Extension point for custom user-provided voice commands."""

from __future__ import annotations

import logging

logger = logging.getLogger("jarvis.commands.custom")


def register(router) -> None:
    """Register custom commands.

    Keep this file as the extension point where advanced users can add new
    keyword-to-action mappings. The design encourages keeping each voice command
    implementation as a reusable callback instead of packing everything into one
    file.
    """
    router.register("custom command", lambda cmd: "Custom command handler available")
