#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:32:48 2025

@author: xenon
"""

import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Fixed variable name "botton" -> "button"
button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)

# Fixed "tk.tk.Button" -> "tk.Button"
close = tk.Button(
    frame,
    text="Quit",
    command=root.quit  # `quit` can be used, but `root.quit` is safer
)
close.pack(side=tk.LEFT)

root.mainloop()
