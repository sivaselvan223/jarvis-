from __future__ import annotations

import logging
import subprocess

logger = logging.getLogger("jarvis.commands.jiosaavn")


def open_jiosaavn(command: str) -> str:
    try:
        subprocess.Popen(
            ["cmd", "/c", "start", "https://www.jiosaavn.com"]
        )
        return "Opening JioSaavn"
    except Exception:
        logger.exception("Failed to open JioSaavn")
        return "Unable to open JioSaavn"


def register(router):
    router.register("open jiosaavn", open_jiosaavn)
    router.register("open jio saavn", open_jiosaavn)