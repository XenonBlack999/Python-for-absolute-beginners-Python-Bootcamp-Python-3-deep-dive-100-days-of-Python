#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:44:34 2025

@author: xenon
"""


def combine_lists(list1: list, list2: list) -> list:
    """
    Combine two lists into a list of tuples using the zip() function.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list of tuples, where each tuple contains one element
              from list1 and one from list2.
    """
    return list(zip(list1, list2))


def unzip_pairs(pairs: list) -> tuple:
    """
    Unzip a list of tuples back into two separate lists.

    Args:
        pairs (list): A list of (x, y) tuples.

    Returns:
        tuple: Two lists — one containing all first elements,
               and one containing all second elements.
    """
    return tuple(map(list, zip(*pairs))) if pairs else ([], [])


# Example usage (optional, remove for automated tests)
if __name__ == "__main__":
    a = [1, 2, 3]
    b = ["A", "B", "C"]

    zipped = combine_lists(a, b)
    print("Zipped:", zipped)

    unzipped = unzip_pairs(zipped)
    print("Unzipped:", unzipped)
