"""Media playback command handlers."""

from __future__ import annotations

import logging

logger = logging.getLogger("jarvis.commands.media")


def register(router) -> None:
    """Register media playback commands."""
    router.register("play music", lambda cmd: "Playing music")
    router.register("pause music", lambda cmd: "Pausing music")
    router.register("next song", lambda cmd: "Playing next song")
    router.register("previous song", lambda cmd: "Playing previous song")
    router.register("brightness control", lambda cmd: "Brightness is managed through Windows settings")
