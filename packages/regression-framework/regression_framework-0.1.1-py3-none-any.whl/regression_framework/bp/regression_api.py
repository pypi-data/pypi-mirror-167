#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" deepNLU Regression API """


from typing import Callable

from baseblock import BaseObject

from regression_framework.svc import LoadRegressionTests
from regression_framework.svc import FilterRegressionTests
from regression_framework.svc import RunRegressionTests


class RegressionAPI(BaseObject):
    """ deepNLU Regression API """

    def __init__(self,
                 find_runner: Callable,
                 find_comparator: Callable):
        """ Change Log

        Created:
            6-Jun-2022
            craigtrim@gmail.com
        Updated:
            13-Sept-2022
            craigtrim@gmail.com
            *   migrated to regression-framework repo

        Args:
            find_runner (Callable): Find the appropriate regression test runner on a per test-case level
            find_comparator (Callable): Find the appropriate regression test comparator on a per test-case level
        """
        BaseObject.__init__(self, __name__)
        self._load_test_cases = LoadRegressionTests().process
        self._filter_test_cases = FilterRegressionTests().process
        self._run_test_cases = RunRegressionTests(
            find_runner=find_runner,
            find_comparator=find_comparator).process

    def process(self,
                test_case_location: str = None) -> None:

        test_cases = self._load_test_cases(test_case_location)
        if not test_cases or not len(test_cases):
            return None

        test_cases = self._filter_test_cases(test_cases)
        if not test_cases or not len(test_cases):
            return None

        test_cases = self._run_test_cases(test_cases)
        if not test_cases or not len(test_cases):
            return None
