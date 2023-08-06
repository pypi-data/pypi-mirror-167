#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Execute a specified Comparator on a Regression Case """


from typing import Callable

from baseblock import BaseObject


class RegressionExecuteComparator(BaseObject):
    """ Execute a specified Comparator on a Regression Case """

    def __init__(self):
        """ Change Log

        Created:
            6-Jun-2022
            craigtrim@gmail.com
        Updated:
            13-Sept-2022
            craigtrim@gmail.com
            *   migrated to regression-framework repo

        Args:
            comparator (Callable): Callback to the regression test comparator
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                actual_results: object,
                expected_results: object,
                comparator: Callable) -> bool:

        return comparator(
            actual_results=actual_results,
            expected_results=expected_results)
