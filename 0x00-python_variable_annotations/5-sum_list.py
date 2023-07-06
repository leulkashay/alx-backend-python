#!/usr/bin/env python3
"""
a typed-annotation function
"""
from typing import List



def sum_list(input_list: List[float]) -> float:
    """
    sum list of float
    """
    sum = 0
    for item in input_list:
        sum += item

    return sum
