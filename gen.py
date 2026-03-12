### GEN.PY

import os
import requests
import json



def generate(api_key = None, inquiry = None, drawm_cards = None, spread = None):
    if inquiry is None:
        print("no inquiry in generate.")
        return
    if api_key is None:
        print("no api_key in generate.")
        return "NO API KEY"
    if drawm_cards is None:
        print("no drawn_cards in generate.")
        return
    if spread is None:
        print("no spread in generate.")
        return



    model_name = "gemini-2.5-flash" 
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"


    headers = {'Content-Type': 'application/json'}


    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": inquiry}]
        }],
        "systemInstruction": {
            "parts": [{"text": f"You will provide an answer for the users inquiry using the {spread} spread. Here are the drawn cards: {drawm_cards}"}]
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
