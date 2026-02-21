### GEN.PY



import os
import requests
import json


def generate(inquiry=None):
    if inquiry is None:
        inquiry = "Am I gonna be ok?"
        
    #api_key = os.environ.get("GEMINI_API_KEY")
    try:
        with open(".key.key","r") as f:
            api_key = f.read()
            f.close()
    except Exception as e:
        print(e)
        api_key = None
        return
        
    #api_key = f"{a1}{a2}"
    # Using the v1beta endpoint for "Thinking" features or v1 for standard
    model_name = "gemini-2.5-flash" 
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"

    headers = {'Content-Type': 'application/json'}
    
    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": inquiry}]
        }],
        "systemInstruction": {
            "parts": [{"text": "You are a tarot card reader. You are insightful yet completely honest. You answer questions completely and directly."}]
        },
        "generationConfig": {
            "temperature": 1.0, # Thinking models usually prefer lower temp than 1.95
            "maxOutputTokens": 2048
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # Navigating the JSON response structure
        if 'candidates' in data and len(data['candidates']) > 0:
            return data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "The Oracle is silent. (No response content)"
            
    except Exception as e:
        return f"Error contacting the cosmic realm: {str(e)}"
