from textblob import TextBlob
from sanitize import get_file, load_data, sanitize_data

# Convert a string into a specified language
def convert_to_language(text, lang):
    textblob = TextBlob(text)
    return textblob.translate(to = lang)

# Translate a string into another language and back again
def roundtrip_translation(text, lang, startingLang):
    newText = convert_to_language(text, lang).string
    return convert_to_language(newText, startingLang)

# Check if a string can go through a round trip translation
# and come back exactly the same
def is_perfect_translation(text, lang, startingLang):
    try:
        return text == roundtrip_translation(text, lang, startingLang)
    except:
        return False

def count_perfect_translations_for_language(tList, lang, initialLang):
    return [is_perfect_translation(x, lang, initialLang) for x in tList].count(True)
