#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" deepNLU Regression API """


from baseblock import EnvIO
from baseblock import BaseObject


from regression_framework.svc import LoadRegressionTests
from regression_framework.svc import FilterRegressionTests
from regression_framework.svc import RunRegressionTests


class RegressionAPI(BaseObject):
    """ deepNLU Regression API """

    def __init__(self):
        """ Change Log

        Created:
            6-Jun-2022
            craigtrim@gmail.com
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)
        self._load_test_cases = LoadRegressionTests().process
        self._filter_test_cases = FilterRegressionTests().process
        self._run_test_cases = RunRegressionTests().process

    def process(self) -> None:

        test_cases = self._load_test_cases()
        if not test_cases or not len(test_cases):
            return None

        test_cases = self._filter_test_cases(test_cases)
        if not test_cases or not len(test_cases):
            return None

        test_cases = self._run_test_cases(test_cases)
        if not test_cases or not len(test_cases):
            return None
