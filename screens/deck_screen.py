from models import RiderDeck, RiderTarotCard
from custom_widgets import FlippableCard


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.carousel import MDCarousel



class DeckScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rd = RiderDeck()
        self.deck = rd.get_deck()
        self.flippable_deck = []
        for c in self.deck:
            fc = FlippableCard(c)
            self.flippable_deck.append(fc)
        

    def on_enter(self):
        self.refresh_carousel()
        super().on_enter()
    

    def refresh_carousel(self):
        for card in self.flippable_deck:
            self.ids.tarot_carousel.add_widget(card)


    @property
    def app(self):
        return MDApp.get_running_app()