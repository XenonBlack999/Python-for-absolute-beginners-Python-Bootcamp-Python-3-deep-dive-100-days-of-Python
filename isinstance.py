#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:46:46 2025

@author: xenon
"""


def check_data_type(value) -> str:
    """
    Check the data type of a given value using isinstance().

    Args:
        value: Any Python object.

    Returns:
        str: A message describing the value's data type.
    """
    if isinstance(value, int):
        return "The value is an Integer."
    elif isinstance(value, float):
        return "The value is a Float."
    elif isinstance(value, str):
        return "The value is a String."
    elif isinstance(value, list):
        return "The value is a List."
    elif isinstance(value, dict):
        return "The value is a Dictionary."
    elif isinstance(value, tuple):
        return "The value is a Tuple."
    else:
        return "Unknown data type."


# Example usage (optional, remove for automated tests)
if __name__ == "__main__":
    print(check_data_type(10))
    print(check_data_type(3.14))
    print(check_data_type("Hello"))
    print(check_data_type([1, 2, 3]))
    print(check_data_type({"key": "value"}))
