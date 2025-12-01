#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:42:16 2025

@author: xenon
"""

# exercise.py

def multiply_by_two(numbers: list) -> list:
    """
    Multiply every number in the list by 2 using the map() function.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list where each number is multiplied by 2.
    """
    return list(map(lambda x: x * 2, numbers))


# Example usage (optional, remove for automated tests)
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    result = multiply_by_two(data)
    print("Original:", data)
    print("Multiplied by 2:", result)
