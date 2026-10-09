"""Command dispatch layer.

The command router receives normalized user text and delegates to dedicated
modules under the commands package. New commands can be added by extending the
routing table or adding a command module class.
"""

from __future__ import annotations

import importlib
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger("jarvis.core.command_router")


class CommandRouter:
    """Classifies commands and dispatches to command handlers."""

    def __init__(self) -> None:
        self.handlers: Dict[str, Any] = {}
        self._register_default_handlers()

    def _register_default_handlers(self) -> None:
        """Register all built-in command modules that are present in this package."""
        modules = [
            "commands.app_control",
            "commands.bluetooth",
            "commands.browser",
            "commands.calculator",
            "commands.chatgpt",
            "commands.clipboard",
            "commands.custom_commands",
            "commands.files",
            "commands.media",
            "commands.reminder",
            "commands.screenshots",
            "commands.spotify",
            "commands.jiosaavn",
            "commands.system",
            "commands.volume",
            "commands.weather",
            "commands.whatsapp",
            "commands.wifi",
            "commands.youtube",
        ]

        for module_name in modules:
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "register"):
                    module.register(self)
                    logger.info("Registered command module %s", module_name)
                else:
                    logger.warning("Command module %s does not expose register()", module_name)
            except Exception as exc:
                logger.exception("Unable to import command module %s: %s", module_name, exc)

    async def route(self, command_text: str) -> str:
        """Find and execute a command."""
        normalized = command_text.strip().lower()
        for keyword, handler in self.handlers.items():
            if keyword in normalized:
                try:
                    if hasattr(handler, "execute"):
                        result = handler.execute(normalized)
                        if result:
                            return str(result)
                    elif callable(handler):
                        result = handler(normalized)
                        if result:
                            return str(result)
                    else:
                        result = handler
                        if result:
                            return str(result)
                except Exception as exc:
                    logger.exception("Router execution failed for %s", keyword, exc)
                    return "I hit a command error"

        return ""

    def register(self, keyword: str, handler: Any) -> None:
        """Register a keyword-level command object or callback."""
        self.handlers[keyword] = handler
