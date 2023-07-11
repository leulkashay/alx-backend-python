#!/usr/bin/env python3
"""
Asynchronous comperhension
"""
from typing imoirt List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension
    """
    return [i async for i in async_generator()]
