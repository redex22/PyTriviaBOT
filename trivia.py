import requests


class Trivia:

    def __init__(self):
        self._first_trivia = requests.get("https://the-trivia-api.com/api/questions").json()[0]
        self._answers = set()
        self.correct_answer()
        self.wrong_answers()

    def random_question(self):
        return self._first_trivia["question"]

    def correct_answer(self):
        self._answers.add(self._first_trivia["correctAnswer"])
        return self._first_trivia["correctAnswer"]

    def wrong_answers(self):
        incorrect_answ = [option for option in self._first_trivia["incorrectAnswers"]]
        self._answers.update(incorrect_answ)
        return self._first_trivia["incorrectAnswers"]

    def get_answers(self):
        return self._answers


if __name__ == "__main__":
    recent_trivia = Trivia()
    print(recent_trivia.random_question())
    print(recent_trivia.correct_answer())
    print(recent_trivia.wrong_answers())
    print(f"Question: {recent_trivia.random_question()}\nAnswers: {', '.join(recent_trivia.get_answers()).rstrip()}")
