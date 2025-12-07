#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 04:57:25 2025

@author: xenon
"""

import json 
myjson : str = """{

"name" : "Xenon",
"age" : 24 ,
"job": "developmer",
"hobby": ["coding","trainning","learning"]



}"""


with open("jdata.json", "w") as  jsonFile:
    json.dump(myjson, jsonFile)
    
#you can check your data in https://jsonlint.com/

