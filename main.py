from random import sample
from tweepy import Cursor, API
from translator import translate_to_spanish
from TweepyHandler import tweet_api
from trivia import Trivia


TODAY_TRIVIA = Trivia()
TWEET_API = tweet_api()


def question_tweet_format(answers: list[str], question: str) -> str:
    multiple_options = sample(answers, len(answers))
    return f"""Today trivia question is:
{question}
And the options are:
1. {multiple_options[0]}
2. {multiple_options[1]}
3. {multiple_options[2]}
4. {multiple_options[3]}
"""


def answer_tweet_format(correct_answer: str) -> str:
    return f"""And the answer to today trivia is (drums please!):
....
{correct_answer}
"""


def question_tweet(api: API, tweet: str):
    return api.update_status(tweet)


def answer_tweet(api: API, tweet: str, tweet_id: str):
    return api.update_status(tweet, in_reply_to_status_id=tweet_id)


def last_tweet_id(api: API):
    for tweet in Cursor(api.home_timeline, result_type="recent").items(1):
        return tweet._json["id"]


def main():
    try:
        global TODAY_TRIVIA
        eng_question = question_tweet_format(list(TODAY_TRIVIA.get_answers()), TODAY_TRIVIA.random_question())
        esp_question = translate_to_spanish(eng_question)
        eng_answer = answer_tweet_format(TODAY_TRIVIA.correct_answer())
        esp_answer = translate_to_spanish(eng_answer)

        question_tweet(TWEET_API, eng_question)
        answer_tweet(TWEET_API, eng_answer, last_tweet_id(TWEET_API))

        question_tweet(TWEET_API, esp_question)
        answer_tweet(TWEET_API, esp_answer, last_tweet_id(TWEET_API))
    except Exception as e:
        TODAY_TRIVIA = Trivia()
        main()
        pass


if __name__ == "__main__":
    main()
