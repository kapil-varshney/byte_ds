#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('master.db')
cursor = connection.cursor()

cursor.execute(
    '''INSERT INTO users(username,
    password, 
    first_name, 
    last_name
    ) 
    VALUES(
    "kv", 
    "blah", 
    "Kapil", 
    "Varshney"
    );'''
)

connection.commit()
cursor.close()
connection.close()