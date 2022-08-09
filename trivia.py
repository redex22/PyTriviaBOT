import requests


class Trivia:
    attributes = requests.get("https://the-trivia-api.com/api/questions").json()
    multiple_options = []

    @classmethod
    def random_question(cls):
        for attribute in cls.attributes:
            return attribute["question"]

    @classmethod
    def correct_answer(cls):
        for attribute in cls.attributes:
            cls.multiple_options.append(attribute["correctAnswer"])
            return attribute["correctAnswer"]

    @classmethod
    def incorrect_answers(cls):
        for attribute in cls.attributes:
            for option in attribute["incorrectAnswers"]:
                cls.multiple_options.append(option)
            return attribute["incorrectAnswers"]

