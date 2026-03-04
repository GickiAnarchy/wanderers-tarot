from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from screens import TarotScreenManager
from screens import ALL_SCREENS


class TarotApp(App):
    def build(self):
        tsm = TarotScreenManager()
        tsm.set_up()
        return tsm
    
