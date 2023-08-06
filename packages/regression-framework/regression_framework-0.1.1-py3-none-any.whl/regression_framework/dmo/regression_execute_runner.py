#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute a specified Runner on a Regression Case """


from typing import Callable

from baseblock import BaseObject


class RegressionExecuteRunner(BaseObject):
    """ Execute a specified Runner on a Regression Case """

    def __init__(self):
        """ Change Log

        Created:
            6-Jun-2022
            craigtrim@gmail.com
        Updated:
            13-Sept-2022
            craigtrim@gmail.com
            *   migrated to regression-framework repo
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                ontologies: list,
                d_test_case: dict,
                runner: Callable) -> object:

        return runner(
            ontologies=ontologies,
            input_text=d_test_case['input'])
