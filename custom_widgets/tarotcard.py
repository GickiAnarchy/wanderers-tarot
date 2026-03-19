from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.widget import MDWidget


class KivyTarotCard(MDWidget):
    """
    A visual tarot card widget that can be placed anywhere in the UI.
    """

    # Card identity
    name = StringProperty("")
    arcana = StringProperty("")      # Major / Minor
    suit = StringProperty("")        # Cups, Wands, etc
    rank = StringProperty("")        # Ace, Two, King, etc

    # Meaning
    upright_meaning = ListProperty([])
    reversed_meaning = ListProperty([])
    keywords = ListProperty([])

    # State
    reversed = BooleanProperty(False)
    revealed = BooleanProperty(False)

    # Optional metadata
    image = StringProperty("")
    number = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def reveal(self):
        """Reveal the card."""
        self.revealed = True

    def flip(self):
        """Flip between upright and reversed."""
        self.reversed = not self.reversed

    def meaning(self):
        """Return the current meaning depending on orientation."""
        if self.reversed:
            return "\n".join(self.reversed_meaning)
        return "\n".join(self.upright_meaning)

    def on_release(self):
        """
        Called when the card is tapped.
        """
        if not self.revealed:
            self.reveal()

    def get_info(self):
        ret = f"Name:\t{self.name}\nMeaning:\t{self.meaning}"
        return ret