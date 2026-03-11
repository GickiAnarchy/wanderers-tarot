### GEN.PY

import os
import requests
import json



def generate(api_key = None, inquiry = None, cards_info = None):
    if inquiry is None or api_key is None:
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
            "parts": [{"text": f"Answer the inquiry using the Tarot with these dealt cards: {cards_info}"}]
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
