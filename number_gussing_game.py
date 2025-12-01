#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:03:44 2025

@author: xenon
"""
import random
import time
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")



def random_number_generator():
    print("Do you need to guss between 1 and 20")
    response2 = input("Input your number:")
    time.sleep(2)
    random_number = random.randint(1, 20)
    print("Our Lucky number was", random_number)
    
    if response2 == random_number:
        print ("You win !")
    else :
        print("You lose because our lucky number was:", random_number)
        
    

def main():
    print("This is Random Number Generator Game")
    print("Type ""clear"" when you want to clear terminal")
    response = input ("Are you ready to start?[y/n]:")
    response = response.lower()
    
    if response == 'y':
        print("We are now starting game!")
        time.sleep(3)
        clear_terminal()
        random_number_generator()
        
    elif response == "clear" or "Clear":
        clear_terminal()
    
    else:
        print("Exiting........")
        exit(0)
        
while True:
    main()