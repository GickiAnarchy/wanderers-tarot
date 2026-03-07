
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard


class TarotCard(ButtonBehavior, MDCard):
    """
    A visual tarot card widget that can be placed anywhere in the UI.
    """

    # Card identity
    name = StringProperty("")
    arcana = StringProperty("")      # Major / Minor
    suit = StringProperty("")        # Cups, Wands, etc
    rank = StringProperty("")        # Ace, Two, King, etc

    # Meaning
    upright_meaning = ListProperty(None)
    reversed_meaning = ListProperty(None)
    keywords = ListProperty(None)

    # State
    reversed = BooleanProperty(False)
    revealed = BooleanProperty(False)

    # Optional metadata
    image = StringProperty("")
    number = NumericProperty(0)

    def reveal(self):
        """Reveal the card."""
        self.revealed = True

    def flip(self):
        """Flip between upright and reversed."""
        self.reversed = not self.reversed

    def meaning(self):
        """Return the current meaning depending on orientation."""
        if self.reversed:
            return self.reversed_meaning
        return self.upright_meaning

    def on_release(self):
        """
        Called when the card is tapped.
        """
        if not self.revealed:
            self.reveal()

