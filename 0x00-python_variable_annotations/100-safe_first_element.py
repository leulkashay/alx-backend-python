#!/usr/bin/env python3
"""
Duck types
"""
from typing imprt Any, Sequence, Tuple, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    duck-type annotation
    """
    if lst:
        return lst[0]
    else:
        return None
