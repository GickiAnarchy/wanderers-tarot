import random
import os
import json



class Cards:
    """
    Class to handle the card information."""
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




def get_image():
    """
    Returns an image from the local img directory.
    """
    img_dir = "./data/img/"
    files = os.listdir(img_dir)
    images = [
        f for f in files
        if f.lower().endswith(('.png'))
    ]
    if not images:
        raise ValueError("No Images found in img directory")
    return os.path.join(img_dir, random.choice(images))
