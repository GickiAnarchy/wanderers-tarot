import json
from fpdf import FPDF
import os

def create_tarot_pdf(json_data_str, output_file_name="tarot_card_details.pdf"):
    """
    Reads tarot card data from a JSON string and writes it to a PDF document,
    with one card per page, using a Unicode-compatible font.

    Args:
        json_data_str (str): A string containing the JSON data of tarot cards.
        output_file_name (str): The name of the output PDF file to create.
    """
    try:
        tarot_data = json.loads(json_data_str)
    except json.JSONDecodeError:
        print("Error: Could not decode JSON data. Please check the content of the file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while parsing JSON data: {e}")
        return

    if not isinstance(tarot_data, list):
        print("Warning: The JSON data is not a list. Attempting to convert if it's a dictionary of cards.")
        if isinstance(tarot_data, dict) and all(isinstance(val, dict) for val in tarot_data.values()):
            tarot_data = list(tarot_data.values())
        else:
            print("Error: The JSON data structure is not supported. It should be a list of card objects.")
            return

    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15) # Enable auto page breaks with a margin

    # --- START OF CHANGES FOR FONT ---
    # Add the Unicode font
    # Ensure 'DejaVuSansCondensed.ttf' and 'DejaVuSansCondensed-Bold.ttf' (if you have it)
    # are in the same directory as this script.
    try:
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        # If you also downloaded the bold version, uncomment and use the line below:
        # pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
    except RuntimeError as e:
        print(f"Error loading font: {e}. Make sure 'DejaVuSansCondensed.ttf' (and -Bold.ttf if used) is in the script directory.")
        print("Falling back to Arial (may not support all Unicode characters and might cause previous error).")
        # Fallback to Arial if the DejaVu font cannot be loaded.
        # Note: Arial.ttf and arialbd.ttf also need to be available on your system or in the script directory.
        pdf.set_font("Arial", "B", 12)
        pdf.set_font("Arial", "", 12)


    # Add a title page
    pdf.add_page()
    pdf.set_font("Arial", "B", 24) # Changed to DejaVu font
    pdf.cell(0, 20, "The Tarot Card Compendium", 0, 1, "C")
    pdf.set_font("DejaVu", "", 12) # Changed to DejaVu font
    pdf.ln(10)
    pdf.multi_cell(0, 10, "This document provides detailed information for each tarot card, with one card per page for easy reference.")

    # Iterate through each card and add to PDF
    for i, card in enumerate(tarot_data):
        # Basic validation for essential keys
        if not all(key in card for key in ['name', 'suit', 'meanings']):
            print(f"Skipping card {i+1} due to missing essential keys (name, suit, or meanings). Card data: {card}")
            continue

        pdf.add_page() # New page for each card
        pdf.set_font("Arial", "B", 18) # Changed to DejaVu font
        pdf.cell(0, 10, f"{card.get('name', 'N/A')} ({card.get('number', 'N/A')})", 0, 1, "C")
        pdf.ln(5)

        pdf.set_font("DejaVu", "", 12) # Changed to DejaVu font
        pdf.write(5, f"Arcana: {card.get('arcana', 'N/A')}\n")
        pdf.write(5, f"Suit: {card.get('suit', 'N/A')}\n")
        pdf.write(5, f"Elemental: {card.get('Elemental', 'N/A')}\n")
        if 'Archetype' in card:
            pdf.write(5, f"Archetype: {card.get('Archetype', 'N/A')}\n")
        if 'Numerology' in card:
            pdf.write(5, f"Numerology: {card.get('Numerology', 'N/A')}\n")
        pdf.ln(8)

        # Keywords
        if 'keywords' in card and card['keywords']:
            pdf.set_font("Arial", "B", 14) # Changed to DejaVu font
            pdf.write(7, "Keywords:\n")
            pdf.set_font("DejaVu", "", 12) # Changed to DejaVu font
            pdf.multi_cell(0, 6, ", ".join(card['keywords']))
            pdf.ln(5)

        # Meanings
        if 'meanings' in card:
            meanings = card['meanings']
            if 'light' in meanings and meanings['light']:
                pdf.set_font("Arial", "B", 14) # Changed to DejaVu font
                pdf.write(7, "Meanings (Light/Upright):\n")
                pdf.set_font("DejaVu", "", 12) # Changed to DejaVu font
                for meaning in meanings['light']:
                    pdf.multi_cell(0, 6, f"• {meaning}")
                pdf.ln(5)

            if 'shadow' in meanings and meanings['shadow']:
                pdf.set_font("Arial", "B", 14) # Changed to DejaVu font
                pdf.write(7, "Meanings (Shadow/Reversed):\n")
                pdf.set_font("DejaVu", "", 12) # Changed to DejaVu font
                for meaning in meanings['shadow']:
                    pdf.multi_cell(0, 6, f"• {meaning}")
                pdf.ln(5)

        # Affirmation
        if 'Affirmation' in card:
            pdf.set_font("Arial", "B", 14) # Changed to DejaVu font
            pdf.write(7, "Affirmation:\n")
            pdf.set_font("DejaVu", "", 12) # Changed to DejaVu font
            pdf.multi_cell(0, 6, card['Affirmation'])
            pdf.ln(5)

    # Output the PDF
    pdf.output(output_file_name)
    print(f"Successfully created '{output_file_name}' with tarot card details.")
    print(f"The file is located at: {os.path.abspath(output_file_name)}")

# --- Main execution part ---
if __name__ == "__main__":
    file_path = "tarot_deck.json" # Still targeting .json as per your original file type

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tarot_json_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please ensure it's in the same directory as the script.")
        tarot_json_content = None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        tarot_json_content = None

    if tarot_json_content:
        create_tarot_pdf(tarot_json_content)
