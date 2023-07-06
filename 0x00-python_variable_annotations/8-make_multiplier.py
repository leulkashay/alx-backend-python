#!/usr/bin/env python3
"""
typed-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a functin that mulitplies a float by multiplier
    """
    def fn(n: float) -> float:
        """
        Multiply a float by multiplier
        """
        return n * multiplier
    return fn
