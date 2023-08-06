# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find a Random Question """


from random import sample

from baseblock import BaseObject

from journal_prompts.dto import list_of_questions


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
        return sample(list_of_questions, 1)[0]
