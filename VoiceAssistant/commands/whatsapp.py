from __future__ import annotations

import os
import time
import pyautogui
import pyperclip


def open_whatsapp(command):
    os.system("start whatsapp:")
    return "Opening WhatsApp"


def send_message(command):
    os.system("start whatsapp:")
    time.sleep(5)  # Wait for WhatsApp to open

    text = command.lower().replace("send message to", "").strip()

    try:
        name, message = text.split(" ", 1)
    except ValueError:
        return "Please say the contact name and message."

    # Open search
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)

    # Search contact
    pyperclip.copy(name)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("enter")

    time.sleep(1)

    # Type message
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    return f"Message sent to {name}"


def register(router):
    router.register("open whatsapp", open_whatsapp)
    router.register("send message to", send_message)