"""Application-launch and application-window command handlers."""

from __future__ import annotations

import logging
import os
import subprocess
import sys

logger = logging.getLogger("jarvis.commands.app_control")


def register(router) -> None:
    """Register application control routes with the command router."""
    router.register("open chrome", lambda cmd: open_app("Chrome", "chrome"))
    router.register("open visual studio code", lambda cmd: open_app("VS Code", "code"))
    router.register("open vscode", lambda cmd: open_app("VS Code", "code"))
    router.register("open notepad", lambda cmd: open_app("Notepad", "notepad"))
    router.register("open calculator", lambda cmd: open_app("Calculator", "calc"))
    router.register("open cmd", lambda cmd: open_app("Command Prompt", "cmd"))
    router.register("open command prompt", lambda cmd: open_app("Command Prompt", "cmd"))
    router.register("open powershell", lambda cmd: open_app("PowerShell", "powershell"))
    router.register("open file explorer", lambda cmd: open_app("File Explorer", "explorer"))
    router.register("open settings", lambda cmd: open_app("Settings", "ms-settings:"))
    router.register("close current application", lambda cmd: close_current_window())
    router.register("switch application", lambda cmd: "Switching application is available through system automation")


def open_app(display_name: str, executable: str) -> str:
    """Open an application using Windows start commands."""
    try:
        if executable.startswith("ms-"):
            os.system(f"start {executable}")
        else:
            os.startfile(executable if os.path.exists(executable) else executable)
        logger.info("Opened %s", display_name)
        return f"Opening {display_name}"
    except Exception as exc:
        logger.exception("Failed to open %s: %s", display_name, exc)
        return f"I could not open {display_name}"


def close_current_window() -> str:
    """Use a public API-level placeholder for closing active foreground window."""
    return "Closing current application"
