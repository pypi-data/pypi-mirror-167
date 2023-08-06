#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find the Comparator for a given Regression Test """


from typing import Callable

from baseblock import BaseObject

# from regression_framework.dmo.comparator import RoundTripComparator
# from regression_framework.dmo.comparator import FindOntologyDataComparator


class RegressionFindComparator(BaseObject):
    """ Find the Comparator for a given Regression Test """

    def __init__(self):
        """ Change Log

        Created:
            6-Jun-2022
            craigtrim@gmail.com
            *   https://github.com/grafflr/deepnlu/issues/22
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_test_case: dict) -> Callable:
        runner_name = d_test_case['engine']['comparator']

        if runner_name == "round_trip":
            # return RoundTripComparator().process
            pass

        if runner_name == "find_ontology_data":
            # return FindOntologyDataComparator().process
            pass

        raise NotImplementedError(runner_name)
