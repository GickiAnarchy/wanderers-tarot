import google.generativeai as genai
import os

# Configure your API key
# It's best practice to load your API key from an environment variable for security.
# For example: export GOOGLE_API_KEY="YOUR_API_KEY" in your terminal
# Or, you can directly assign it here for testing purposes (not recommended for production):
# genai.configure(api_key="YOUR_API_KEY")

# If using environment variable:
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    print("Please set the GOOGLE_API_KEY environment variable.")
    exit()

def get_tarot_interpretation(user_question, card_names):
    """
    Generates a tarot card interpretation using the Gemini API.

    Args:
        user_question (str): The question asked by the user.
        card_names (list): A list of the names of the drawn tarot cards.

    Returns:
        str: The AI-generated interpretation.
    """
    model = genai.GenerativeModel('gemini-pro') # You can choose other models like 'gemini-1.5-flash' if available and suitable

    # Construct the prompt for the AI
    prompt = f"The user asked: '{user_question}'\n" \
             f"The drawn tarot cards are: {', '.join(card_names)}.\n" \
             "Please provide a meaningful interpretation of these cards in relation to the user's question, offering guidance and insight."

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Example Usage:
def example():
    question = "What should I focus on in my career next year?"
    cards = ["The Empress", "The Wheel of Fortune", "The Hermit"]

    interpretation = get_tarot_interpretation(question, cards)
    print(interpretation)


#############################

if __name__ == "__main__":
    example()
    #generate()
