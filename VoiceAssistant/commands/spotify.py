from __future__ import annotations

import logging
import subprocess
import webbrowser
import os
from urllib.parse import quote_plus

logger = logging.getLogger("jarvis.commands.spotify")

SPOTIFY_EXE = os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WindowsApps\Spotify.exe"
)


def open_spotify(command: str) -> str:
    try:
        subprocess.Popen([SPOTIFY_EXE])
        logger.info("Spotify opened")
        return "Opening Spotify"
    except Exception:
        logger.exception("Failed to open Spotify")
        webbrowser.open("https://open.spotify.com")
        return "Opening Spotify Web"


def play_spotify(command: str) -> str:
    query = (
        command.lower()
        .replace("play spotify", "")
        .replace("search spotify", "")
        .strip()
    )

    if query == "":
        return open_spotify(command)

    open_spotify(command)

    url = f"https://open.spotify.com/search/{quote_plus(query)}"
    webbrowser.open(url)

    return f"Searching Spotify for {query}"


def register(router) -> None:
    router.register("spotify", open_spotify)
    router.register("open spotify", open_spotify)
    router.register("launch spotify", open_spotify)
    router.register("start spotify", open_spotify)

    router.register("play spotify", play_spotify)
    router.register("search spotify", play_spotify)