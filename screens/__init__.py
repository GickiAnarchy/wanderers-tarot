from .rootcontroller import RootController
from .tarot_screen import TarotScreen
from .settings_screen import SettingsScreen
from .home_screen import HomeScreen
from .reading_screen import ReadingScreen
from .history_screen import HistoryScreen



ALL_SCREENS = [
    (HomeScreen,"home"),
    (TarotScreen,"tarot"),
    (SettingsScreen,"settings"),
    (ReadingScreen, "reading"),
    (HistoryScreen, "history"),
]


__all__ = [
    "RootController",
    "HomeScreen",
    "TarotScreen",
    "SettingsScreen",
    "ReadingScreen",
    "HistoryScreen",
]