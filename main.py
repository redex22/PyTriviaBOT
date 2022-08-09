import os
import random
import tweepy
from translator import translate_to_spanish
from trivia import Trivia
from dotenv import load_dotenv
load_dotenv()


todays_trivia = Trivia()
question = todays_trivia.random_question()
right_answer = todays_trivia.correct_answer()
wrong_answers = todays_trivia.incorrect_answers()
answers = todays_trivia.multiple_options


def twepy():
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth)
    return api


def format_trivia(question=question, multiple_options=answers):
    multiple_options = random.sample(multiple_options, len(multiple_options))
    return f"""Today trivia question is:
{question}
And the options are:
1. {multiple_options[0]}
2. {multiple_options[1]}
3. {multiple_options[2]}
4. {multiple_options[3]}
"""


def format_answer(correct_answer=right_answer):
    return f"""And the answer to today trivia is (drums please!):
....
{correct_answer}
"""


def question_tweet():
    return twepy().update_status(format_trivia())


def answer_tweet():
    return twepy().update_status(format_answer())


def esp_question_tweet():
    return twepy().update_status(translate_to_spanish(format_trivia()))


def esp_answer_tweet():
    return twepy().update_status(translate_to_spanish(format_answer()))


if __name__ == "__main__":
    question_tweet()
    answer_tweet()
    esp_question_tweet()
    esp_answer_tweet()
