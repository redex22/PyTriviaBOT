from translate import Translator
from triviaScraping import questions


def translate_to_spanish(string):
    translator = Translator(from_lang="en", to_lang="es")
    translation = translator.translate(string)
    return translation


if __name__ == "__main__":
    print(translate_to_spanish(questions[0]))