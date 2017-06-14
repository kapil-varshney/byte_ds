#!/usr/bin env python3

import sqlite3


conn = sqlite3.connect("terminal_trading.db")
cur = conn.cursor()


cur.execute("""
            CREATE TABLE users(
            username VARCHAR PRIMARY KEY,
            password VARCHAR,
            name VARCHAR,
            user_type VARCHAR DEFAULT "user",
            balance FLOAT DEFAULT 100000
            );"""
)

cur.execute("""
            CREATE TABLE stocks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol VARCHAR,
            stock_name VARCHAR,
            exchange VARCHAR,
            last_price FLOAT,
            quantity INTEGER,
            user VARCHAR,
            FOREIGN KEY(user) REFERENCES users(username)
            );"""
)

cur.execute("""
            CREATE TABLE transactions(
            transact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            buy_sell VARCHAR,
            symbol VARCHAR,
            transact_price FLOAT,
            quantity INTEGER,
            user VARCHAR,
            FOREIGN KEY(user) REFERENCES users(username)
            );"""
)

conn.commit()
cur.close()
conn.close()