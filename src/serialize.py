import json
import os
import base64
import datetime
from PIL import Image
from .cardsjson import number_strings
from .page_creator import savePage


deck_json = r"src/tarot_deck.json"

#
#
#TAROT DECK I/O
def load_tarot_deck():
    deck = []
    with open(deck_json,"r") as file:
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
    with open(deck_json,"w") as file:
        json.dump(deck, file, indent = 2)
    print("Tarot Deck Saved")

#
#
# READINGS I/O
readfile = r"src/past_readings.json"
def save_readings(reading):
    with open(readfile,"a") as f:
        json.dump(reading, f, indent = 2)
        f.close()

def save_ai_reading(reading):
    #savePage(reading)
    with open(f"src/readings/reading.json", "a") as f:
        json.dump(reading, f, indent = 2)
        f.close()

def load_readings():
    if not os.path.exists("src/readings/reading.json"):
        return
    with open("src/readings/reading.json", "r") as f:
        data = json.load(f)
        #data = f.read()
        f.close()
    return data

#
#
#IMAGE COBVERSION
img_path = r"img/"

def encode_img():
    for file in os.listdir(img_path):
        name = ""
        en_str = ""
        if file.endswith(".png"):
            name = file[:-4]
    #Open the image:
        with open(f"{img_path}{file}", "rb") as image_file:
            #image = Image.open(image_file)
            #Encode to base64:
            en_str = base64.b64encode(image_file.read())
        with open(f"img/.{name}.b64","w") as f:
            f.write(en_str.decode("utf-8"))
            f.close()
        
def decode_img():
    for k in os.listdir(img_path):
        if not k.endswith(".b64"):
            continue
        with open(f"{img_path}{k}","rb") as f:
            decoded = f.read()
            f.close()
            decodeit = open(f"{img_path}{k[1:-4]}.png", "wb")
            decodeit.write(base64.b64decode((decoded)))

#
#
def writeHTML(reading):
    pass