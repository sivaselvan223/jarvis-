"""Bluetooth controls."""

from __future__ import annotations

import logging
import subprocess

logger = logging.getLogger("jarvis.commands.bluetooth")


def open_bluetooth(command: str) -> str:
    try:
        subprocess.run(
            ["explorer.exe", "ms-settings:bluetooth"],
            shell=True
        )
        return "Opening Bluetooth settings"
    except Exception as e:
        logger.exception(e)
        return "Unable to open Bluetooth settings"


def register(router):
    router.register("bluetooth", open_bluetooth)
    router.register("open bluetooth", open_bluetooth)
    router.register("turn bluetooth on", open_bluetooth)
    router.register("turn bluetooth off", open_bluetooth)
    router.register("bluetooth on", open_bluetooth)
    router.register("bluetooth off", open_bluetooth)