#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:32:48 2025

@author: xenon
"""

import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()
