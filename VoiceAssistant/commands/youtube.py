"""YouTube command handlers."""

from __future__ import annotations

import logging
import webbrowser
from urllib.parse import quote_plus

logger = logging.getLogger("jarvis.commands.youtube")


def search_youtube(command: str) -> str:
    query = command.lower().replace("search youtube", "").strip()

    if not query:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
    webbrowser.open(url)
    return f"Searching YouTube for {query}"


def play_video(command: str) -> str:
    query = (
        command.lower()
        .replace("play first video", "")
        .replace("play youtube", "")
        .replace("play", "")
        .strip()
    )

    if not query:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    url = (
        f"https://www.youtube.com/results?search_query="
        f"{quote_plus(query)}&sp=EgIQAQ%253D%253D"
    )

    webbrowser.open(url)
    return f"Playing {query} on YouTube"


def open_youtube(command: str) -> str:
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube"


def register(router) -> None:
    router.register("youtube", open_youtube)
    router.register("open youtube", open_youtube)
    router.register("search youtube", search_youtube)
    router.register("play youtube", play_video)
    router.register("play first video", play_video)
