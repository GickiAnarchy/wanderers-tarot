from .rootcontroller import RootController
from .screens import HomeScreen, TarotScreen
from .settings_screen import SettingsScreen

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