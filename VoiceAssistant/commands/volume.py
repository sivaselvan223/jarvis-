"""Volume and audio device command handlers."""

from __future__ import annotations

import logging

logger = logging.getLogger("jarvis.commands.volume")


def register(router) -> None:
    """Register volume-related routes."""
    router.register("increase volume", lambda cmd: "Increasing volume")
    router.register("decrease volume", lambda cmd: "Decreasing volume")
    router.register("mute", lambda cmd: "Muting audio")
    router.register("unmute", lambda cmd: "Unmuting audio")
