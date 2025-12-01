#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 3 02:28:08 2025

@author: xenon
"""

def add(x, y):
    z = x + y
    print("Your Adding two numbers result is:", z)
    
def sub(x, y):
    z = x - y
    print("Your subtraction two numbers result is:", z)
    
def multi(x, y):
    z = x * y
    print("Your multiplication two numbers result is:", z)
    
def division(x, y):
    if y != 0:
        z = x / y
        print("Your division two numbers result is:", z)
    else:
        print("Error: Division by zero is not allowed.")

def main():
    print("This is Python Calculator!")
    response = input("Do you want to start? [y/n]: ").lower()
    
    if response == 'y':
        try:
            x = float(input("Input your first number: "))
            y = float(input("Input your second number: "))
            w = input("Input your operation (+, -, x, /): ")
            
            if w == '+':
                add(x, y)
            elif w == '-':
                sub(x, y)
            elif w == 'x':
                multi(x, y)
            elif w == '/':
                division(x, y)
            else:
                print("Invalid operation. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif response == 'n':
        print("Exiting the calculator. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

while True:
    main()
