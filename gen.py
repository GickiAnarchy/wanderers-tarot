### GEN.PY



import os
import requests
import json


def generate(inquiry=None):
    if inquiry is None:
        inquiry = "Am I gonna be ok?"
        
    try:
        with open(".key.key","r") as f:
            api_key = f.read()
            f.close()
    except Exception as e:
        print(e)
        api_key = None
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
            "parts": [{"text": "You're a tarot card reader. Answer questions completely."}]
        },
        "generationConfig": {
            "temperature": 0.9, # Thinking models usually prefer lower temp than 1.95
            "maxOutputTokens": 3500
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        with open("saved.json","w") as f:
            json.dump(data, f, indent=4)
        
        # Navigating the JSON response structure
        if 'candidates' in data and len(data['candidates']) > 0:
            return data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "The Oracle is silent. (No response content)"
            
    except Exception as e:
        return f"Error contacting the cosmic realm: {str(e)}"
