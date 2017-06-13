#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE persons(
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128),
    nickname VARCHAR(128),
    dob VARCHAR(128)
    );'''
)
cursor.execute(
    '''CREATE TABLE laptops(
    laptop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model VARCHAR(128),
    ram VARCHAR(128),
    person INTEGER,
    FOREIGN KEY(person) REFERENCES persons(person_id)
    );'''
)

connection.commit()
cursor.close()
connection.close()


