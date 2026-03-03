import os
import json



class Cards:
    def __init__(self):
        self.file_name = "cards.json"
        with open(self.file_name, "r") as f:
            data = json.load(f)
            self.cards = {c.get('name'): c for c in data}

    def get_desc(self, cards):
        desc = [f"{c}\nKeywords: {self.cards[c].get('keywords')}" for c in cards]
        return "-----".join(desc)

    @property
    def card_names(self):
        return list(self.cards.keys())
