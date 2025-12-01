#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:36:27 2025

@author: xenonblack
"""

class shark:
    species = "Callorhinchidae"
    
    def __init__(self, name, genus):
        self.name = name
        self.genus = genus
        
        
shark1 = shark("ghost shark", "Callorhinchus milii")
shark2 = shark("blacknose shark", "Carcharhinus acronotus")
shark3 = shark("silvertip shark", "Carcharhinus albimarginatus")


print(shark1.name)
print(shark1.genus)
print(shark1.species)
print("\n")

print(shark2.name)
print(shark2.genus)
print(shark2.species)
print("\n")

print(shark3.name)
print(shark3.genus)
print(shark3.species)
print("\n")

shark.species = "Alopiidae"

print(shark1.species)
print(shark2.species)
print(shark3.species)

