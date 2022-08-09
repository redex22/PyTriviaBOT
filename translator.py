from translate import Translator


def translate_to_spanish(string):
    translator = Translator(from_lang="en", to_lang="es")
    translation = translator.translate(string)
    return translation

