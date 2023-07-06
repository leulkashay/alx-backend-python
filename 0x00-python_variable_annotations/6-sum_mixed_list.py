#!/usr/bin/env python3
"""
functipn annotation
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Sum float and int togothere
    and return float
    """
    return float(sum(mxd_list))
