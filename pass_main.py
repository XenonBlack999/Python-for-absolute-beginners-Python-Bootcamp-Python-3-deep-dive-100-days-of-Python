#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 02:11:18 2025

@author: xenon
"""


import sqlite3
import os
from tabulate import tabulate
import binascii

def creating_db():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS password (webname TEXT, name TEXT, password TEXT)")
    con.commit()
    con.close()
    print("Done!")
    
    
def check_update(webname, name, password):
    if not os.path.exists("tutorial.db"):
        creating_db()
        print("Database is not have but we create now!")
    else:
        insert_data(webname, name, password)
        

def insert_data(webname, name, password):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("INSERT INTO password (webname, name, password) VALUES (?, ?, ?)", 
                (webname, name, password))
    con.commit()
    con.close()
    print("Data Inserted Successfully!")


def show_all_passwords():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    data = list(cur.execute("SELECT webname, name, password FROM password ORDER BY webname"))
    con.close()
    if data:
        print(tabulate(data, headers=["Website", "Username", "Password"], tablefmt="grid"))
    else:
        print("No stored credentials found.")
        
        
def retrieve_password(webname):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    
    cur.execute("SELECT name, password FROM password WHERE webname=?", (webname,))
    
    result = cur.fetchone()
    
    if result:
        print(f"Website: {webname}")
        print(f"Username: {result[0]}")
        print(f"Password: {result[1]}")
    else:
        print(f"No credentials found for {webname}.")
    
    con.close()

def action():
    action_menu = """
    1.Storing new password
    2.Finding my passsword with website name
    3.Checking all password 
    """
    print(action_menu)
    response = input("Input your function name:")
    
    if response == '1':
        webname = input ("Input your Website name :")
        name = input ("Input your user name or email:")
        password = input ("Input your Password:")
        insert_data(webname, name, password)
        
    elif response == '2':
        webname = input("Input the website name to retrieve password: ")
        retrieve_password(webname)
        
    elif response == '3':
        show_all_passwords()
    
    else:
        print("Something wroung in upper step ,Please Try again!")
        
        

def main():
    key = input ("Input your key:")
    key2 = binascii.b2a_base64(("{}".format(key)).encode())
    en_key = b'eGVub25AMTIz\n'
    if key2 == en_key:
        print("Success we are starting now.....")
        action()
    else:
        print("You wroung!")
        pass
    
    

        
if __name__ == "__main__":
    main()