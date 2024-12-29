from transformers import pipeline

# Load the Hugging Face translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ar-en")

def translate_to_english(text: str) -> str:
    """
    Translates Arabic text to English using Hugging Face.
    """
    result = translator(text, max_length=512)
    return result[0]['translation_text']
