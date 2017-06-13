#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('master.db')
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE users(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(128),
    password VARCHAR(128),
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    phone_number VARCHAR(128),
    email VARCHAR(128)
    )'''
)