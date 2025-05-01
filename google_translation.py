from deep_translator import GoogleTranslator

# Text to be translated
text_to_translate = input("Enter the text to translate: ")

# Prompt for the target language code
target_language = input("Enter the target language code (e.g., 'es' for Spanish): ")

# Translate the text
translated = GoogleTranslator(source='auto', target=target_language).translate(text_to_translate)

# Output the translated text
print(f"Original Text: {text_to_translate}")
print(f"Translated Text: {translated}")
