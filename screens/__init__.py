from .tarotmanager import TarotScreenManager
from .input_screen import InputScreen
from .readingscreen import ReadingScreen
from .keyscreen import KeyScreen


ALL_SCREENS = [
    (InputScreen, "input"),
    (ReadingScreen, "reading"),
    (KeyScreen, "key"),
]


__all__ = [
    "TarotScreenManager",
    "InputScreen",
    "ReadingScreen",
    "KeyScreen",
]