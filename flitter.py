#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:43:08 2025

@author: xenon
"""


def filter_even_numbers(numbers: list) -> list:
    """
    Filter and return only the even numbers from a list using filter().

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing only the even integers.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))


# Example usage (optional, remove for automated tests)
if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5, 6]
    result = filter_even_numbers(sample_data)
    print("Original list:", sample_data)
    print("Even numbers:", result)
