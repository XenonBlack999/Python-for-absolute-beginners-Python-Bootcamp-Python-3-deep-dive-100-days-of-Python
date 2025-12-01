#partial function 
def myfun(x,y,z):
    print(x,y,z)
    
def pfn(yy,zz):
    return myfun(10,yy,zz)

print(pfn(111, 222))


#!/usr/bin/env python3
#partial function from functools
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 03:12:39 2025

@author: xenon
"""

from functools import partial

def myfun(x,y,z):
    x = x + 11
    y = y + 22
    z = z + 33
    print(x,y,z)
    
newfun= partial(myfun, 10)

newfun(100,200)
