import os
import json

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty,ListProperty


class HistoryScreen(MDScreen):
    history = ListProperty([])
    
    
    def on_pre_enter(self):
        self.refresh()
    
    
    def refresh(self):
        history = self.app.rc.load_history()
        
        self.ids.history_list.clear_widgets()
        if not history:
            self.ids.history_list.add_widget(OneLineListItem(text="There is no past"))
            return
        for reading in history:
            inq = reading.get("inquiry")
            label = MDLabel(text=inq)
            item = OneLineListItem(text=inq,on_release=lambda x, r=reading: self.open_reading(r))
            self.ids.history_list.add_widget(item)

    
    def open_reading(self, reading):
        ps = self.manager.get_screen("past")
        ps.update_screen(reading)
        self.manager.current = "past"
    
    
    @property
    def app(self):
        return MDApp.get_running_app()
    