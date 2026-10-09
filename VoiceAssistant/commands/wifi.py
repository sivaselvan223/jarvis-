"""Wi-Fi and internet connection helpers."""

from __future__ import annotations

import logging
import subprocess

logger = logging.getLogger("jarvis.commands.wifi")


def register(router) -> None:
    """Register Wi-Fi commands with the router."""
    router.register("turn wifi on", lambda cmd: "Turning Wi-Fi on")
    router.register("turn wifi off", lambda cmd: "Turning Wi-Fi off")
    router.register("wifi on", lambda cmd: "Turning Wi-Fi on")
    router.register("wifi off", lambda cmd: "Turning Wi-Fi off")
    router.register("check internet speed", lambda cmd: check_speed())


def check_speed() -> str:
    """Return a placeholder internet speed response."""
    return "Internet speed check is available through a network diagnostic module"
