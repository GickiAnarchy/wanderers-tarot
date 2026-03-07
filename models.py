from custom_widgets import TarotCard
import os
import json
import random


class TarotCards:    
    def __init__(self):
        self.card_file = "cards.json"
        self.card_data = self.read_json()
        self.cards = []
        self.create_cards()

    def create_cards(self):
        self.cards = []
        if self.card_data:
            for c in self.card_data:
                tc = TarotCard()
                tc.name = c.get("name")
                tc.number = c.get("number")
                tc.arcana = c.get("arcana")
                tc.suit = c.get("suit")
                tc.upright_meaning = c["meanings"].get("light")
                tc.reversed_meaning = c["meanings"].get("shadow")
                tc.keywords = c.get("keywords")

                self.cards.append(tc)
            self.shuffle()

    def shuffle(self):
        if self.cards:
            for c in self.cards:
                c.reversed = random.choices([True,False])
            random.shuffle(self.cards)

    def read_json(self) -> dict:
        if not os.path.exists(self.card_file):
            return
        try:
            with open(self.card_file, "r") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(e)
            return {}

    def draw_cards(self, amount:int):
        for c in range(amount):
            if self.cards:
                yield self.cards.pop()


