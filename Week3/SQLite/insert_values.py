#!/usr/bin/env/ python3

import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
"""
cursor.execute(
    '''
    INSERT INTO persons(
    name,
    nickname,
    dob
    ) 
    VALUES(
    "Kapil",
    "kv",
    "14-10-1990"
    );'''
)

cursor.execute(
    '''
    INSERT INTO persons(
    name,
    nickname,
    dob
    ) 
    VALUES(
    "Anitej",
    "Ani",
    "21-02-1995"
    );'''
)

cursor.execute(
    '''
    INSERT INTO persons(
    name,
    nickname,
    dob
    ) 
    VALUES(
    "Uday",
    "Ud",
    "06-02-1992"
    );'''
)
"""

cursor.execute(
    '''
    INSERT INTO laptops(
    model,
    ram,
    person
    )
    VALUES(
    'Lenovo',
    '16gb',
    1
    );'''
)

cursor.execute(
    '''
    INSERT INTO laptops(
    model,
    ram,
    person
    )
    VALUES(
    'Asus',
    '2gb',
    1
    );'''
)

cursor.execute(
    '''
    INSERT INTO laptops(
    model,
    ram,
    person
    )
    VALUES(
    'MacBook Pro',
    '8gb',
    2
    );'''
)

cursor.execute(
    '''
    INSERT INTO laptops(
    model,
    ram,
    person
    )
    VALUES(
    'MacBook Pro',
    '4gb',
    3
    );'''
)

connection.commit()
cursor.close()
connection.close()
