from textblob import TextBlob
from sanitize import get_file, load_data, sanitize_data

# Convert a string into a specified language
def convert_to_language(text, lang):
    textblob = TextBlob(text)
    return textblob.translate(to = lang)

# Translate a string into another language and back again
# Note that we have to use .string to get the string object
# before passing it to the next convert_to_language function
# Otherwise a type error will be thrown
def roundtrip_translation(text, lang, startingLang):
    newText = convert_to_language(text, lang).string
    return convert_to_language(newText, startingLang).string

# Check if a string can go through a round trip translation
# and come back exactly the same
#
# Note that the translation library may throw an error if the
# text is not translatable, in that case we return False to
# symbolise a failed round trip translation
def is_perfect_translation(text, lang, startingLang):
    try:
        return text == roundtrip_translation(text, lang, startingLang)
    except:
        return False

# Return the number of perfect translations for each string
# in the tList (the file as an array) using the target language
# and initial language
def count_perfect_translations_for_language(tList, lang, initialLang):
    return [is_perfect_translation(x, lang, initialLang) for x in tList].count(True)
