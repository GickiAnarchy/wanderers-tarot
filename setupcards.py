import os
import json
from tarot import TarotCard
from cardsjson import major_cards, number_strings
from serialize import load_tarot_deck, save_tarot_deck

def fromjson():
    tarot_deck = load_tarot_deck()
    """with open("tarot-images.json","r") as f:
        tarot_data = json.load(f)
        f.close()
    for c_details in tarot_data:
        tarot_deck.append(TarotCard(**c_details))"""
    for c in tarot_deck:
        c.display()
    save_tarot_deck(tarot_deck)


def initialize():
    tarot_deck = []
    majors = major_cards
    minors = []
    suits = ["Moons","Feathers","Stones","Knives"]
    
    t_cards = []
    for card_details in majors:
        tc = TarotCard(**card_details)
        tc.display()
        t_cards.append(tc)

    majors = t_cards
    
    for s in suits:
        for i,v in number_strings.items():
            if i == 0:
                continue
            n = f"{number_strings[i]} of {s}"
            card = TarotCard(name=n, number=str(i), suit=s)
            minors.append(card)

    tarot_deck = majors + minors
    tarot_json = []
    
    for c in tarot_deck:
        c.display()
        tarot_json.append(c.getDict())
    
    with open("tarot_deck.json","w") as file:
        json.dump(tarot_json, file, indent = 2)
    print(f"WANDERERS TAROT DECK ({str(len(tarot_json))} cards) CREATED")

if __name__ == "__main__":
    fromjson()
    """if os.path.exists("tarot_deck.json"):
        print("We exist")
    else:
        initialize()"""
 