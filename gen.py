# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate(inquiry=None, spread = None):
    instruct = ""
    if inquiry is None:
        inquiry = "Am I gonna be ok?"
        
        if spread == "celtic":
            if os.path.exists("celtic_cross.txt"):
                with open("celtic_cross.txt","r") as f:
                    instruct = f.read()
                    
        if spread == None:
            instruct = "Only do a 3 card reading. (Only use 3 of the cards drawn)"
        
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=inquiry),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1.95,
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        system_instruction=[
            types.Part.from_text(text="You are a tarot card reader. You are insightful yet completely honest. You answer the questions and inquiries of seekers while keeping things brief and to the point"),
        ],
    )

    full_response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
        if chunk.text:
            full_response += chunk.text

    return full_response
        

if __name__ == "__main__":
    generate()


