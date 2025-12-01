#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:39:19 2025

@author: xenonblack
"""

from zipfile import ZipFile, BadZipFile
import argparse


parser = argparse.ArgumentParser(description="\n Usage : Python zipbrute.py -z <zipfile.zip> -p <passwordfile.txt>")
parser.add_argument("-z", dest="ziparchive", help="zip archive file")
parser.add_argument("-p", dest="passfile", help="password file")
parsed_args = parser.parse_args()


if not parsed_args.ziparchive or not parsed_args.passfile:
    print("Error: Missing required arguments.")
    print(parser.description)
    exit(1)

try:

    with ZipFile(parsed_args.ziparchive) as ziparchive:
        passfile = parsed_args.passfile
        foundpass = None

        with open(passfile, "r") as f:
            for line in f:
                password = line.strip("\n") 

                try:
                 
                    ziparchive.setpassword(password.encode("utf-8"))

                    ziparchive.testzip()

                   
                    foundpass = password
                    print(f"Password found: {foundpass}")
                    break 

                except RuntimeError:
                    continue

        if not foundpass:
            print("Password not found in the list.")
        else:
            print(f"Password for zip file: {foundpass}")

except BadZipFile:
    print("Error: The file is not a valid zip file.")
except Exception as e:
    print(f"Error: {e}")
    exit(0)
