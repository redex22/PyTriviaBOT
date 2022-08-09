import requests
import random


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


if __name__ == "__main__":
    #print(Trivia)
    print(Trivia.random_question())
    print(Trivia.correct_answer())
    print(Trivia.incorrect_answers())
    print(Trivia.multiple_options)
    randQ = random.sample(Trivia.multiple_options, len(Trivia.multiple_options))
    print(randQ)