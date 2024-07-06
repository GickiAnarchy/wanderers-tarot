import json
import os
from cardsjson import number_strings

def load_tarot_deck():
    deck = []
    with open("tarot_deck.json","r") as file:
        data = json.load(file)
        for card_details in data:
            yield card_details
        file.close()

def save_tarot_deck(deck_to_save):
    deck = []
    i = 0
    for card in deck_to_save:
        i += 1
        deck.append(card.getDict(exclude_attributes =["Questions to Ask","img","Hebrew Alphabet","Mythical/Spiritual"]))
        print(str(i))
    with open("tarot_deck.json","w") as file:
        
        json.dump(deck, file, indent = 2)
    print("Tarot Deck Saved")
    

readfile = r"past_readings.json"
def save_readings(reading):
    with open(readfile,"a") as f:
        json.dump(reading, f, indent = 2)
        #f.write(reading)
        f.close()

def load_readings():
    if not os.path.exists(readfile):
        return
    with open(readfile, "r") as f:
        #data = json.load(f)
        data = f.read()
        f.close()
    return data