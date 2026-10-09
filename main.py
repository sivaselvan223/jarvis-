"""Repository root launcher for the VoiceAssistant package.

This file enables the exact command-line contract expected by the user:
    python main.py
from the workspace root, instead of forcing the caller to drop into the
VoiceAssistant package directory first.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "VoiceAssistant"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from main import JarvisApp


if __name__ == "__main__":
    app = JarvisApp()
    app.run()
