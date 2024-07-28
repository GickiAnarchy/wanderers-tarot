import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from src.serialize import save_ai_reading
from google.colab import userdata

import google.generativeai as genai

key_won = "AIzaSyAYIhfVoQAjqwj"
key_too = "XVfwNtAWbNafmyillPWA"

genai.configure(api_key=f"{key_won}{key_too}")

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
    safety_settings = {HarmCategory.HARM_CATEGORY_HARASSMENT:HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_HATE_SPEECH:HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT:HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:HarmBlockThreshold.BLOCK_NONE},
    system_instruction = "You are a wandering nomad who has traveled the world over the last 80 years. You have great interest in the tarot and enjoy reading the tarot to help answer questions for people. You go by the name 'Journey'. You are sometimes melancholic, sometimess optimistic, but always nostalgic. Explain each card and then a brief overall summary of the entire reading regarding the question asked.")

chat_session = model.start_chat(history=[])


ppf_positions = [
    "",
    "The past",
    "The present",
    "The future"]

def pastPresentFuture(reading):
    cds = ""
    i = 0
    cds_list = reading.getCards()
    for d in cds_list:
        i += 1
        cds += f"{str(i)}){ppf_positions[i]}:{d}"
    result = f"The seeker has asked a queston and you, as the reader,  read the seekers tarot in the 3 card past, present, future spread from the following question and cards:"
    result += f"Question:{reading.question}"
    result += f"Cards:{cds}"
    response = chat_session.send_message(result)
    response_to_save = {
        "date_and_time":reading.getTime(),
        "question":reading.question,
        "cards_drawn":cds,
        "response":response.text
    }
    save_ai_reading(response_to_save)
    return response.text


#
celtic_positions = [
    "",
    "The Seeker / The situation in question.",
    "What crosses or complements the seeker.",
    "The best that can be achieved in the circumstances.",
    "The foundation: The reason for the reading.",
    "The past.",
    "The near future.",
    "The seeker.",
    "Seekers enviroment-External influences affecting the seeker.",
    "Hopes or Fears.",
    "The outcome."
    ]

def celticCross(reading):
    cds = ""
    i = 0
    cds_list = reading.getCards()
    for d in cds_list:
        i += 1
        cds += f"{str(i)}){celtic_positions[i]}:{d}"
    result = f"The seeker has asked a queston and you, as the reader,  read the seekers tarot in the celtic cross spread from the following question and cards:\n\tQuestion:{reading.question}\n\tCards:{cds}"
    response = chat_session.send_message(result)
    response_to_save = {
        "date_and_time":reading.getTime(),
        "question":reading.question,
        "cards_drawn":cds,
        "response":response.text
    }
    save_ai_reading(response_to_save)
    return response.text

tree_positions = [
    "",
    "Your situation",
    "Responsibilities",
    "Limitations and the past",
    "What supports you",
    "What opposes you",
    "Achievements",
    "Attraction and relationships",
    "Work, health, and communication",
    "What is hidden",
    "The future environment, the outcome"
    ]

def treeOfLife(reading):
    cds = []
    i = 0
    cds_list = reading.getCards()
    for d in cds_list:
        i += 1
        cds.append(f"{str(i)}){tree_positions[i]}:{d}")
    result = f"The seeker has asked a queston and you, as the reader,  read the seekers tarot in the Tree Of Life spread from the following question and cards:"
    result += "\n"
    result += f"Question:{reading.question}"
    joined_cds = '\n'.join(cds)
    result += f"Cards:{joined_cds}"
    response = chat_session.send_message(result)
    print(dict(response))
    response_to_save = {
        "date_and_time":reading.getTime(),
        "question":reading.question,
        "cards_drawn":cds,
        "response":response.text
    }
    save_ai_reading(response_to_save)
    return response.text
 
    
if __name__ == "__main__":
    #An even simpler test to see this script works at all. Run this file directly to execute this, as it won't run when imported!
    print(gemrequest(input("Text to send: ")))
