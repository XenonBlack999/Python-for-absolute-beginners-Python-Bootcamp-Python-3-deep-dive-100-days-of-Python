#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:47:24 2025

@author: xenon
"""



def check_any(values: list) -> str:
    """
    Check if ANY value in the list is True using the any() function.

    Args:
        values (list): A list containing any type of values.

    Returns:
        str: A message describing the result of any().
    """
    if any(values):
        return "At least one value is True."
    else:
        return "No True values found."


def check_all(values: list) -> str:
    """
    Check if ALL values in the list are True using the all() function.

    Args:
        values (list): A list containing any type of values.

    Returns:
        str: A message describing the result of all().
    """
    if all(values):
        return "All values are True."
    else:
        return "Not all values are True."


# Example usage (optional, remove for automated tests)
if __name__ == "__main__":
    print(check_any([0, False, 5, None]))
    print(check_any([0, False, 0]))

    print(check_all([1, True, 3]))
    print(check_all([1, 0, True]))
