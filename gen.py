### GEN.PY
from models import TarotCards, RiderDeck, RiderTarotCard

import os
import requests
import json






def generate(api_key = None, inquiry = None):
    if inquiry is None:
        print("no inquiry in generate.")
        return
    if api_key is None:
        print("no api_key in generate.")
        return "NO API KEY"


    model_name = "gemini-2.5-flash" 
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"


    headers = {'Content-Type': 'application/json'}


    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": inquiry}]
        }],
        "systemInstruction": {
            "parts": [{"text": f"You will provide an answer for the users inquiry using the Celtic Cross spread."}]
        },
        "generationConfig": {
            "temperature": 0.9,
            "maxOutputTokens": 3500
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if 'candidates' in data and len(data['candidates']) > 0:
            return data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "The Oracle is silent. (No response content)"

    except Exception as e:
        return f"Error contacting the cosmic realm: {str(e)}"




def generate_celtic_cross(api_key = None, inquiry = None):
    print("generate_celtic_cross()")
    if inquiry is None:
        print("no inquiry in generate.")
        return
    if api_key is None:
        print("no api_key in generate.")
        return "NO API KEY"

    tc = TarotCards()
    cards = tc.draw_cards(10)
    meanings = tc.get_meanings(cards)

    model_name = "gemini-2.5-flash" 
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

    headers = {'Content-Type': 'application/json'}

    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": inquiry}]
        }],
        "systemInstruction": {
            "parts": [{"text": f"Using the tarot, You will provide an answer for the users inquiry using the Celtic Cross spread. Here are the cards drawn with their meanings: {meanings}"}]
        },
        "generationConfig": {
            "temperature": 0.9,
            "maxOutputTokens": 3500
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if 'candidates' in data and len(data['candidates']) > 0:
            return data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "The Oracle is silent. (No response content)"

    except Exception as e:
        return f"Error contacting the cosmic realm: {str(e)}"


def generate_yes_no(api_key = None, inquiry = None):
    print("generate_yes_no()")
    if inquiry is None:
        print("no inquiry in generate.")
        return
    if api_key is None:
        print("no api_key in generate.")
        return "NO API KEY"

    tc = RiderDeck()
    card = tc.get_random_card()
    meanings = card.yes_no
    
    return f"{card.name} would indicate {meanings}"


def check_inquiry(api_key, inquiry):
    model_name = "gemini-2.5-flash" 
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

    headers = {'Content-Type': 'application/json'}

    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": inquiry}]
        }],
        "systemInstruction": {
            "parts": [{"text": f"Can the following inquiry be answered with a simple yes or no?: \n```{inquiry}```\nAnswer with only one word: Just a 'yes' or a 'no'. Nothing more. This is internal and users will not see this response. "}]
        },
        "generationConfig": {
            "temperature": 0.9,
            "maxOutputTokens": 3500
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if 'candidates' in data and len(data['candidates']) > 0:
            answer = data['candidates'][0]['content']['parts'][0]['text']
            
            if answer.lower() == "yes":
                return generate_yes_no(api_key,inquiry)
            if answer.lower() == "no":
                return generate_celtic_cross(api_key, inquiry)
            else:
                return f"Something strange happened.\n\n{answer}"
            
    except Exception as e:
        print(f"Error: {str(e)}")

