from .dto import *
from .svc import *

from .svc.find_random_question import FindRandomQuestion

finder = FindRandomQuestion()


def find_random_question() -> str:
    return finder.find()


def corpus_size() -> int:
    from journal_prompts.dto import list_of_questions
    from journal_prompts.dto import journal_prompts
    from journal_prompts.dto import journal_prompts_random
    return len(list_of_questions) + len(journal_prompts) + len(journal_prompts_random)
