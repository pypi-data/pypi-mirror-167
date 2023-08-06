from .dto import *
from .svc import *

from .svc.find_random_question import FindRandomQuestion

finder = FindRandomQuestion()


def find_random_question() -> str:
    return finder.find()
