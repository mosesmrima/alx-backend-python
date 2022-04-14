#!/usr/bin/env python3
"""
    List of floats annotations
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list: list of floats
    Return:
          float
    """
    result: float = 0
    for x in input_list:
        result += x
    return result
