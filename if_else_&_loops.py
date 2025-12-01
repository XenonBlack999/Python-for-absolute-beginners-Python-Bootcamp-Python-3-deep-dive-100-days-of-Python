#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 07:04:51 2025

@author: xenon
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Control Flow:
if, elif, else, for loop, while loop
Author: Xenon
"""


# --------------------------------------
# 1. IF / ELIF / ELSE STATEMENTS
# --------------------------------------

x = 20

print("IF / ELIF / ELSE Examples:")

if x > 30:
    print("x is greater than 30")
elif x == 20:
    print("x is exactly 20")
else:
    print("x is less than 20")

print("\n")


# --------------------------------------
# 2. FOR LOOP
# --------------------------------------

print("FOR Loop Example:")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)

print("\n")


# Using range() with for loop
print("FOR Loop with range():")
for i in range(1, 6):
    print("Number:", i)

print("\n")


# --------------------------------------
# 3. WHILE LOOP
# --------------------------------------

print("WHILE Loop Example:")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\n")


# --------------------------------------
# 4. BREAK and CONTINUE inside loops
# --------------------------------------

print("BREAK Example:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\n")

print("CONTINUE Example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

print("\n")


# --------------------------------------
# 5. INFINITE LOOP (with break)
# --------------------------------------

print("While loop with break (safe loop):")

num = 1
while True:
    print(num)
    num += 1

    if num > 5:   # stop the infinite loop
        break
