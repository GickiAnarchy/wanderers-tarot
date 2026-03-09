from .rootcontroller import RootController
from .screens import TarotScreen
from .settings_screen import SettingsScreen
from .home_screen import HomeScreen

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