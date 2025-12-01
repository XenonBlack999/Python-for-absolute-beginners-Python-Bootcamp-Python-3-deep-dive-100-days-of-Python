#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 04:53:29 2025

@author: xenonblack
"""

import sys, time,os
import sevseg

secondsLeft = 3600*24

try:
    while True:
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
        
        os.system('clear')
        print(hTopRow + ' ' + mTopRow + '' + sTopRow)
        print(hMiddleRow + '*' + mMiddleRow + '*' + sMiddleRow)
        print(hBottomRow + '*' + mBottomRow + '*' + sBottomRow)
        
        if secondsLeft == 0:
            print()
            print(' ****BOOM***')
            break
        
        print()
        print('Press Ctrl+C to Quit.')
        
        time.sleep(1)
        secondsLeft -= 1
except KeyboardInterrupt:
    print("Count Down By xenon")
    sys.exit()