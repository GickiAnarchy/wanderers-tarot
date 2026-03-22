from .rootcontroller import RootController
from .tarot_screen import TarotScreen
from .settings_screen import SettingsScreen
from .home_screen import HomeScreen
from .reading_screen import ReadingScreen
from .history_screen import HistoryScreen
from .past_screen import PastReading
from .deck_screen import DeckScreen
from .yn_screen import YesOrNoScreen



ALL_SCREENS = [
    (HomeScreen,"home"),
    (TarotScreen,"tarot"),
    (SettingsScreen,"settings"),
    (ReadingScreen, "reading"),
    (HistoryScreen, "history"),
    (PastReading, "past"),
    (DeckScreen, "deck"),
    (YesOrNoScreen, "yn"),
]


__all__ = [
    "RootController",
    "HomeScreen",
    "TarotScreen",
    "SettingsScreen",
    "ReadingScreen",
    "HistoryScreen",
    "PastReading",
    "DeckScreen",
    "YesOrNoScreen",
]