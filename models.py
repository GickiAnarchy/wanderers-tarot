
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
                tc.name = c.get("name","")
                tc.number = c.get("number",0)
                tc.arcana = c.get("arcana","")
                tc.suit = c.get("suit","")
                tc.upright_meaning = c["meanings"].get("light",[])
                tc.reversed_meaning = c["meanings"].get("shadow",[])
                tc.keywords = c.get("keywords",[]),
                tc.image = c.get("image", "")

                self.cards.append(tc)
            self.shuffle()


    def shuffle(self):
        if self.cards:
            for c in self.cards:
                c.reversed = random.choice([True,False])
            random.shuffle(self.cards)


    def read_json(self):
        if not os.path.exists(self.card_file):
            return []
        try:
            with open(self.card_file, "r") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(e)
            return []


    def draw_cards(self, amount:int):
        for c in range(amount):
            if self.cards:
                yield self.cards.pop()
    
    
    def get_meanings(self, card_list):
        meanings = []
        for card in card_list:
            meanings.append(card.get_info())
        return "\n".join(meanings)




class TarotCard:
    def __init__(self, **kwargs):
        self.reversed = True
        try:
            self.name = kwargs.get("name","")
            self.number = kwargs.get("number",0)
            self.arcana = kwargs.get("arcana","")
            suit = kwargs.get("suit","")
            self.upright_meaning = kwargs["meanings"].get("light",[])
            self.reversed_meaning = kwargs["meanings"].get("shadow",[])
            self.keywords = kwargs.get("keywords",[])
        except Exception as e:
            print(f"Error:\
                TarotCard()__init__()\
                {e}")


    @property
    def meaning(self):
        """Return the current meaning depending on orientation."""
        if self.reversed:
            return "\n".join(self.reversed_meaning)
        return "\n".join(self.upright_meaning)


    def get_info(self):
        ret = f"Name:\t{self.name}\nMeaning:\t{self.meaning}"
        return ret




class RiderDeck:
    def __init__(self):
        self.deck = []
        self.create_deck()
        self.shuffle()


    def create_deck(self):
        with open("rider_waite_tarot.json","r") as f:
            data = json.load(f)
        for c in data.get("cards"):
            rc = RiderTarotCard(**c)
            self.deck.append(rc)


    def shuffle(self):
        if self.deck:
            for c in self.deck:
                c.is_reversed = random.choice([True,False])
            random.shuffle(self.deck)
    
    
    def get_deck(self):
        return self.deck




class RiderTarotCard:
    def __init__(self, **kwargs):
        self.name           = kwargs.get("name", "")
        self.id             = kwargs.get("id", None)
        self.arcana         = kwargs.get("arcana", "")
        self.suit           = kwargs.get("suit", None)
        self.number         = kwargs.get("number", "")
        self.roman_numeral  = kwargs.get("roman_numeral", "")
        self.element        = kwargs.get("element", "")
        self.astrological   = kwargs.get("astrological", "")
        self.hebrew_letter  = kwargs.get("hebrew_letter", None)
        self.keywords       = kwargs.get("keywords", [])
        self.upright        = kwargs.get("upright", {})
        self.reversed       = kwargs.get("reversed", {})
        self.description    = kwargs.get("description", "")
        self.imagery_symbols = kwargs.get("imagery_symbols", [])
        self.yes_no         = kwargs.get("yes_no", "")
        self.image          = kwargs.get("image", "")
        
        self.is_reversed = None

    def get_meanings(self):
        ret = ""
        for k,v in self.upright.items():
            ret += f"{k.title()}:\n{v}\n"
        for k,v in self.reversed.items():
            ret += f"{k.title()} (Reversed):\n{v}\n"
        return ret