from .inputscreen import InputScreen
from .readingscreen import ReadingScreen
from .keyscreen import KeyScreen


ALL_SCREENS = [
    (InputScreen, "input"),
    (ReadingScreen, "reading"),
    (KeyScreen, "key"),
]