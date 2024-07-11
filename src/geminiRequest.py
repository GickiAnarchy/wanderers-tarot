from dotenv import load_dotenv
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from src.serialize import save_ai_reading
#So this imports the dotenv file...

load_dotenv()

import google.generativeai as genai

#GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
#Just make sure you have the key in a .env file on your working directory.

#This will initialize the model!
#genai.configure(api_key=GEMINI_API_KEY)

#Here's the actual code that handles whatever you put into the text...
#You can see there is also a maxtoken attribute. Adjust that to your liking!
def gemrequest(prompt, maxtoken = 8000, model = 'gemini-1.5-flash-latest'):
    model = genai.GenerativeModel(model)

    response =  model.generate_content(prompt, generation_config=genai.types.GenerationConfig(max_output_tokens=maxtoken))

    if not (response.prompt_feedback.block_reason == response.prompt_feedback.BlockReason(0)):
        #This means it was blocked from responding due to some reason...
        print("Response blocked. See following for reason:")
        print()
        return (False, response.prompt_feedback)
    else:
        return (True, response.text)

if __name__ == "__main__":
    #An even simpler test to see this script works at all. Run this file directly to execute this, as it won't run when imported!
    print(gemrequest(input("Text to send: ")))


"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  safety_settings = {HarmCategory.HARM_CATEGORY_HARASSMENT:HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_HATE_SPEECH:HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT:HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:HarmBlockThreshold.BLOCK_NONE
  },
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are a spiritual guide and an expert in reading the meaning of tarot cards. "
)

chat_session = model.start_chat(
  history=[
  ]
)

def geminiWT(ask):
    response = chat_session.send_message(ask)
    save_ai_reading(response.text)
    print(response.text)
    return response.text