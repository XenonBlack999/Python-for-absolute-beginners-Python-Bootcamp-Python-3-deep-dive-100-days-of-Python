#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 06:51:35 2025
Author: xenon

Description:
    Demonstration of all basic Python data types
    and how to use the type() function to check them.
"""

# --- String ---
x: str = "Hello, I am a string"
print("x =", x, "->", type(x))

# --- Integer ---
y: int = 12
print("\ny =", y, "->", type(y))

# --- Float ---
z: float = 1.7
print("\nz =", z, "->", type(z))

# --- List (Array) ---
my_list: list = [10, 20, 30, "apple"]
print("\nmy_list =", my_list, "->", type(my_list))

# --- Tuple (Immutable list) ---
my_tuple: tuple = (1, 2, 3, "banana")
print("\nmy_tuple =", my_tuple, "->", type(my_tuple))

# --- Set (No duplicate values) ---
my_set: set = {1, 2, 3, 3, 4}
print("\nmy_set =", my_set, "->", type(my_set))

# --- Dictionary (Key-Value pairs) ---
my_dict: dict = {
    "name": "xenon",
    "age": 22,
    "country": "Myanmar"
}
print("\nmy_dict =", my_dict, "->", type(my_dict))

# --- Boolean ---
is_active: bool = True
print("\nis_active =", is_active, "->", type(is_active))

# --- None Type (No value) ---
nothing = None
print("\nnothing =", nothing, "->", type(nothing))
