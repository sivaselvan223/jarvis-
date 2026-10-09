"""File and folder command handlers."""

from __future__ import annotations

import logging
import os
import shutil
import subprocess
from pathlib import Path

logger = logging.getLogger("jarvis.commands.files")


def open_folder(path: str) -> str:
    try:
        os.startfile(path)
        return f"Opening {Path(path).name}"
    except Exception as e:
        logger.exception(e)
        return "Unable to open folder."


def open_file(path: str) -> str:
    try:
        os.startfile(path)
        return f"Opening {Path(path).name}"
    except Exception as e:
        logger.exception(e)
        return "Unable to open file."


def create_folder(command: str) -> str:
    folder = Path.home() / "JarvisFolder"
    folder.mkdir(parents=True, exist_ok=True)
    return "Folder created successfully."


def delete_folder(command: str) -> str:
    folder = Path.home() / "JarvisFolder"

    if folder.exists():
        shutil.rmtree(folder)
        return "Folder deleted."

    return "Folder not found."


def create_file(command: str) -> str:
    file = Path.home() / "JarvisFile.txt"

    if not file.exists():
        file.write_text("Created by Jarvis")

    return "File created successfully."


def delete_file(command: str) -> str:
    file = Path.home() / "JarvisFile.txt"

    if file.exists():
        file.unlink()
        return "File deleted."

    return "File not found."


def search_file(command: str) -> str:
    name = (
        command.lower()
        .replace("search file", "")
        .replace("find file", "")
        .strip()
    )

    if not name:
        return "Please tell the file name."

    for root, dirs, files in os.walk(Path.home()):
        for file in files:
            if name.lower() in file.lower():
                path = os.path.join(root, file)
                os.startfile(path)
                return f"Opening {file}"

    return "File not found."


def rename_file(command: str) -> str:
    return "Rename feature is ready. Please specify source and new name."


def move_file(command: str) -> str:
    return "Move feature is ready. Please specify source and destination."


def open_explorer(command: str) -> str:
    subprocess.Popen("explorer")
    return "Opening File Explorer."


def register(router):

    # Explorer
    router.register("file explorer", open_explorer)
    router.register("open file explorer", open_explorer)
    router.register("open explorer", open_explorer)

    # Files
    router.register("create file", create_file)
    router.register("delete file", delete_file)
    router.register("search file", search_file)
    router.register("find file", search_file)
    router.register("rename file", rename_file)
    router.register("move file", move_file)

    # Folders
    router.register("create folder", create_folder)
    router.register("delete folder", delete_folder)

    # Common folders
    router.register("open downloads", lambda c: open_folder(str(Path.home() / "Downloads")))
    router.register("open documents", lambda c: open_folder(str(Path.home() / "Documents")))
    router.register("open desktop", lambda c: open_folder(str(Path.home() / "Desktop")))
    router.register("open pictures", lambda c: open_folder(str(Path.home() / "Pictures")))
    router.register("open videos", lambda c: open_folder(str(Path.home() / "Videos")))
    router.register("open music", lambda c: open_folder(str(Path.home() / "Music")))

    # Direct file
    router.register("open file", search_file)