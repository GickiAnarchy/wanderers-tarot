from .rootcontroller import RootController
from .screens import HomeScreen, TarotScreen, SettingsScreen

ALL_SCREENS = [
    (HomeScreen,"home"),
    (TarotScreen,"tarot"),
    (SettingsScreen,"settings"),
]


__all__ = [
    "RootController",
    "HomeScreen",
    "TarotScreen",
    "SettingsScreen",
]