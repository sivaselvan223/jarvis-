"""Calculator command handlers.

This is a lightweight placeholder for calculator execution. In a real release it
can be tied to a desktop calculator, Python expression evaluator, or speech-to-
math workflow.
"""

from __future__ import annotations

import logging

logger = logging.getLogger("jarvis.commands.calculator")


def register(router) -> None:
    """Register calculator command patterns."""
    router.register("calculate", lambda cmd: calculate_expression(cmd))


def calculate_expression(command: str) -> str:
    """Perform a simple arithmetic command if the command includes an expression."""
    try:
        expression = command.replace("calculate", "").replace("what is", "").strip()
        if not expression:
            return "I need a math expression"

        result = eval(expression, {"__builtins__": {}}, {})
        return f"The answer is {result}"
    except Exception as exc:
        logger.warning("Calculator parse error: %s", exc)
        return "I could not evaluate that expression"
