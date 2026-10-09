"""Browser-driven voice commands."""

from __future__ import annotations

import logging
import webbrowser

logger = logging.getLogger("jarvis.commands.browser")


def register(router) -> None:
    """Register browser-based terms."""
    router.register("open google", lambda cmd: open_url("https://www.google.com"))
    router.register("open youtube", lambda cmd: open_url("https://www.youtube.com"))
    router.register("open gmail", lambda cmd: open_url("https://mail.google.com"))
    router.register("open github", lambda cmd: open_url("https://github.com"))
    router.register("open linkedin", lambda cmd: open_url("https://linkedin.com"))
    router.register("search for python tutorial", lambda cmd: open_search("python tutorial"))
    router.register("search chatgpt", lambda cmd: open_url("https://chat.openai.com"))
    router.register(
        "open music",
        lambda cmd: open_url("https://apps.microsoft.com/detail/9NBLGGH1RRH1?hl=en-us&gl=IN&ocid=pdpshare"),
    )
    router.register(
        "play music",
        lambda cmd: open_url("https://apps.microsoft.com/detail/9NBLGGH1RRH1?hl=en-us&gl=IN&ocid=pdpshare"),
    )
    router.register(
        "launch music",
        lambda cmd: open_url("https://apps.microsoft.com/detail/9NBLGGH1RRH1?hl=en-us&gl=IN&ocid=pdpshare"),
    )
    router.register(
        "jarvis open music",
        lambda cmd: open_url("https://apps.microsoft.com/detail/9NBLGGH1RRH1?hl=en-us&gl=IN&ocid=pdpshare"),
    )


def open_url(url: str) -> str:
    """Open a URL in the default browser."""
    try:
        webbrowser.open(url, new=2)
        logger.info("Opened browser URL: %s", url)
        return f"Opening {url}"
    except Exception as exc:
        logger.exception("Browser open failed: %s", exc)
        return "I could not open the browser page"


def open_search(query: str) -> str:
    """Perform a generic web search."""
    search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    return open_url(search_url)
