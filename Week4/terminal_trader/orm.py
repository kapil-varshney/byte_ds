#!/usr/bin env python3

import sqlite3


def verify_identity(username, password):
    conn = sqlite3.connect("terminal_trading.db")
    cur = conn.cursor()
    cur.execute('SELECT username FROM users WHERE username = ?',(username,))
    data = cur.fetchone()
    if data is None:
        return False
    else:
        cur.execute('SELECT username FROM users WHERE password = ?', (password,))
        data = cur.fetchone()
        if data is None:
            return False
        else:
            return True


def username_available(username):

    conn = sqlite3.connect("terminal_trading.db")
    cur = conn.cursor()
    cur.execute('SELECT username FROM users WHERE username = ?', (username,))
    data = cur.fetchone()
    if data is None:
        return True
    else:
        return False


def create_users(username, password, name):

    conn = sqlite3.connect("terminal_trading.db")
    cur = conn.cursor()

    cur.execute('INSERT INTO users(username, password, name) VALUES(?,?,?)', (username, password, name,))

    conn.commit()
    cur.close()
    conn.close()


def buy_sell_stocks():

    pass


#create_users()
#print(verify_identity('kv', 'lah'))
#print(username_available('kv'))
#create_users('uk', 'blah', 'Uday')