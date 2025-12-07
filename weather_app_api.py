#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 05:32:58 2025

@author: xenon
"""

import json
import requests


url = "https://api.terraquakeapi.com/v1/earthquakes/recent"


params = {"limit": 10}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    if data.get("success") and "payload" in data and isinstance(data["payload"], list):
        if len(data["payload"]) > 0:
            for event in data["payload"]:
                props = event.get("properties", {})
                magnitude = props.get("mag", "N/A")
                place = props.get("place", "Unknown")
                print(f"{magnitude} - {place}")
        else:
            print("No earthquake data found.")
    else:
        print("Unexpected data format or no payload.")
else:
  print(f"Error: {response.status_code} - {response.text}")
  
  
  
  

      