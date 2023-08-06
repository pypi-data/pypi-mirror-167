# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find a Random Question """


from random import sample

from baseblock import odds_of
from baseblock import BaseObject

from journal_prompts.dto import list_of_questions
from journal_prompts.dto import journal_prompts
from journal_prompts.dto import journal_prompts_random


class FindRandomQuestion(BaseObject):
    """ Find a Random Question """

    def __init__(self):
        """
        Created:
            14-Sept-2022
            craigtrim@gmail.com
        """
        BaseObject.__init__(self, __name__)

    def find(self) -> str:
        if odds_of(75):
            return sample(list_of_questions, 1)[0]

        if odds_of(75):
            return sample(journal_prompts, 1)[0]

        return sample(journal_prompts_random, 1)[0]
