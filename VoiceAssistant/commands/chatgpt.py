from __future__ import annotations

import logging
import webbrowser

logger = logging.getLogger("jarvis.commands.chatgpt")


def open_chatgpt(command: str):
    webbrowser.open("https://chat.openai.com")
    return "Opening ChatGPT"


def register(router):
    router.register("chatgpt", open_chatgpt)
    router.register("chat gpt", open_chatgpt)
    router.register("open chatgpt", open_chatgpt)
    router.register("open chat gpt", open_chatgpt)
    router.register("open ai", open_chatgpt)
    router.register("open a i", open_chatgpt)
    router.register("chat", open_chatgpt)