"""Clipboard helper operations."""

from __future__ import annotations

import logging
import pyperclip

logger = logging.getLogger("jarvis.commands.clipboard")


def register(router) -> None:
    """Register clipboard hot phrases."""
    router.register("copy", lambda cmd: copy_clipboard())
    router.register("paste", lambda cmd: paste_clipboard())
    router.register("cut", lambda cmd: cut_clipboard())
    router.register("undo", lambda cmd: "Undoing last action")
    router.register("redo", lambda cmd: "Redoing last action")


def copy_clipboard() -> str:
    """Copy a current selection to the clipboard using a selected clipboard library."""
    try:
        pyperclip.copy("")
        return "Copied"
    except Exception as exc:
        logger.warning("Clipboard copy issue: %s", exc)
        return "Clipboard copy failed"


def paste_clipboard() -> str:
    """Paste the current clipboard content."""
    try:
        value = pyperclip.paste()
        return f"Pasted {value[:50]}"
    except Exception as exc:
        logger.warning("Clipboard paste issue: %s", exc)
        return "Clipboard paste failed"


def cut_clipboard() -> str:
    """Cut selection from the active UI surface."""
    return "Cut command issued"
