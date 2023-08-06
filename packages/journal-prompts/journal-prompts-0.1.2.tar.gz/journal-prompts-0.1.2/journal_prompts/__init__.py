from .dto import *
from .svc import *

from .svc.find_random_question import FindRandomQuestion

finder = FindRandomQuestion()


def find_random_question() -> str:
    return finder.find()


def corpus_size() -> int:
    from .dto.random_questions_kb import list_of_questions
    return len(list_of_questions)
