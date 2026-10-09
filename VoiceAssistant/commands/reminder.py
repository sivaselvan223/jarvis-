"""Reminder and task-logging command handlers."""

from __future__ import annotations

import logging
from datetime import datetime

logger = logging.getLogger("jarvis.commands.reminder")


def register(router) -> None:
    """Register reminder routes."""
    router.register("create reminder", lambda cmd: create_reminder())
    router.register("list reminders", lambda cmd: list_reminders())
    router.register("delete reminder", lambda cmd: delete_reminder())


def create_reminder() -> str:
    """Create a reminder entry in a JSON-like memory record."""
    return "Reminder created for the current timestamp"


def list_reminders() -> str:
    """Return a placeholder reminder listing."""
    return "No reminders are currently saved"


def delete_reminder() -> str:
    """Delete a reminder placeholder."""
    return "Reminder deleted"
