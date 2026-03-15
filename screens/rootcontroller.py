import json

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from models import TarotCards
from gen import generate
from kivymd.uix.toolbar import MDTopAppBar



class RootController(MDBoxLayout):

    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cards = TarotCards()


    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_"," ").title()
        
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")


    def no_key_warning(self):
        if self.api_key is None:
            self.toolbar.right_action_items = (["warning", None])
            return False            
        else:
            self.toolbar.right_action_items = []
            return True


    @property
    def api_key(self):
        akey = self.screen_manager.get_screen("settings").get_api_key()
        if akey == "":
            return None
        return akey


    @property
    def inquiry(self):
        inq = self.screen_manager.get_screen("tarot").inquiry
        if inq not in ["", None]:
            return inq
        else:
            return None


    def send_inquiry(self, inq, cards_amount:int):
        cards = self.draw_cards(cards_amount)
        c_info = self.get_cards_info(cards)
    
        data = generate(self.api_key, inq, c_info, "Celtic Cross")
        rs = self.screen_manager.get_screen("reading")
        rs.res_label.text = data
        self.screen_manager.current = "reading"


    def draw_cards(self, card_amount:int):
        all_cards = TarotCards()
        cards_drawn = all_cards.draw_cards(card_amount)
        return cards_drawn

    def get_cards_info(self, cards):
        all_info = []
        for c in cards:
            all_info.append(c.get_info())
        return "\n".join(all_info)


    @property
    def app(self):
        return MDApp.get_running_app()