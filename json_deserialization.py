#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 04:57:25 2025

@author: xenon
"""

import json x


myjson_str = """
{
    "name": "Xenon",
    "age": 24,
    "job": "developer",
    "hobby": ["coding","training","learning"]
}
"""

#json_obj = json.loads(myjson_str)
#pretty = json.dumps(json_obj, indent=4)
#print(pretty)


with open("jdata.json", "w") as dataFile:
    json.dump(myjson_str, dataFile)
    
    
    
with open("jdata.json","r") as rDataFile:
    data = json.load(rDataFile) 
print(data)