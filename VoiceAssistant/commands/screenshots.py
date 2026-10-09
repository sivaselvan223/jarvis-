"""Screenshot command handlers."""

from __future__ import annotations

import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger("jarvis.commands.screenshots")

try:
    import pyautogui
except Exception:
    pyautogui = None


def take_screenshot(command: str = "") -> str:
    """Take a screenshot and save it."""

    if pyautogui is None:
        return "PyAutoGUI is not installed."

    try:
        folder = Path(__file__).resolve().parent.parent / "assets" / "screenshots"
        folder.mkdir(parents=True, exist_ok=True)

        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = folder / filename

        image = pyautogui.screenshot()
        image.save(filepath)

        logger.info("Screenshot saved: %s", filepath)

        return f"Screenshot saved at {filepath}"

    except Exception as e:
        logger.exception("Screenshot failed")
        return f"Screenshot failed: {e}"


def register(router) -> None:
    router.register("take screenshot", take_screenshot)
    router.register("capture screenshot", take_screenshot)
    router.register("save screenshot", take_screenshot)
    router.register("take screen shot", take_screenshot)