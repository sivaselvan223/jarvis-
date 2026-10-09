"""System resource and machine-level control commands."""

from __future__ import annotations

import logging
import os
import platform
import shutil
import subprocess
import time

logger = logging.getLogger("jarvis.commands.system")


def register(router) -> None:
    """Register system automation routes."""
    router.register("shutdown pc", lambda cmd: shutdown_system())
    router.register("restart pc", lambda cmd: restart_system())
    router.register("sleep pc", lambda cmd: sleep_system())
    router.register("lock pc", lambda cmd: lock_system())
    router.register("sign out", lambda cmd: sign_out())
    router.register("battery percentage", lambda cmd: battery_info())
    router.register("cpu usage", lambda cmd: cpu_usage())
    router.register("ram usage", lambda cmd: ram_usage())
    router.register("disk usage", lambda cmd: disk_usage())
    router.register("gpu information", lambda cmd: gpu_info())
    router.register("ip address", lambda cmd: ip_address())
    router.register("current time", lambda cmd: current_time())
    router.register("current date", lambda cmd: current_date())


def shutdown_system() -> str:
    """Shutdown the current Windows machine."""
    os.system("shutdown /s /t 0")
    return "Shutting down the PC"


def restart_system() -> str:
    """Restart the current Windows machine."""
    os.system("shutdown /r /t 0")
    return "Restarting the PC"


def sleep_system() -> str:
    """Put the system into sleep mode."""
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
    return "Putting the PC to sleep"


def lock_system() -> str:
    """Lock the current Windows session."""
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking the PC"


def sign_out() -> str:
    """Sign out of Windows."""
    os.system("shutdown /l")
    return "Signing out"


def battery_info() -> str:
    """Return a placeholder battery status response."""
    return "Battery status is not available in this environment"


def cpu_usage() -> str:
    """Return current CPU usage using psutil if available."""
    try:
        import psutil
        return f"CPU usage is {psutil.cpu_percent(interval=1)} percent"
    except Exception as exc:
        logger.warning("Could not read CPU usage: %s", exc)
        return "CPU usage information is unavailable"


def ram_usage() -> str:
    """Return current RAM usage using psutil if available."""
    try:
        import psutil
        mem = psutil.virtual_memory()
        return f"RAM usage is {mem.percent} percent"
    except Exception:
        return "RAM usage information is unavailable"


def disk_usage() -> str:
    """Return disk usage information."""
    try:
        usage = shutil.disk_usage("C:\\")
        total = usage.total / (1024 ** 3)
        used = usage.used / (1024 ** 3)
        return f"Disk usage is {round((used / total) * 100, 1)} percent"
    except Exception:
        return "Disk usage information is unavailable"


def gpu_info() -> str:
    """Return a placeholder GPU status."""
    return "GPU information is not available in the current configuration"


def ip_address() -> str:
    """Return basic host machine IP information."""
    try:
        import socket
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "IP address information is unavailable"


def current_time() -> str:
    """Return current time."""
    import datetime
    return datetime.datetime.now().strftime("%H:%M:%S")


def current_date() -> str:
    """Return current date."""
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d")
