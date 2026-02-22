import os
import random

def get_image():
    img_dir = "./img/"
    files = os.listdir(img_dir)
    images = [
        f for f in files
        if f.lower().endswith(('.png'))
    ]
    if not images:
        raise ValueError("No Images found in img directory")
    return os.path.join(img_dir, random.choice(images))
