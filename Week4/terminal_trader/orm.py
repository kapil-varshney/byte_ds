#!/usr/bin env python3

import sqlite3
import pandas.io.sql as psql


class ORM:

    conn = sqlite3.connect("terminal_trading.db")
    cur = conn.cursor()

    @classmethod
    def verify_identity(cls, username, password):

        cls.cur.execute('SELECT username FROM users WHERE username = ?', (username,))
        data = cls.cur.fetchone()
        if data is None:
            return False
        else:
            cls.cur.execute('SELECT password FROM users WHERE username = ?', (username,))
            cls.conn.commit()
            data = cls.cur.fetchone()
            if data is None:
                return False
            elif data[0] == password:
                return True
            else:
                return False


    @classmethod
    def username_available(cls, username):

        cls.cur.execute('SELECT username FROM users WHERE username = ?', (username,))
        data = cls.cur.fetchone()

        if data is None:
            return True
        else:
            return False


    @classmethod
    def create_users(cls, username, password, name):

        cls.cur.execute('INSERT INTO users(username, password, name) VALUES(?,?,?)', (username, password, name,))
        cls.conn.commit()

    @classmethod
    def retrieve_balance(cls, username):

        cls.cur.execute('SELECT balance FROM users WHERE username = ?', (username,))
        balance = cls.cur.fetchone()[0]
        cls.conn.commit()

        return balance

    @classmethod
    def update_transactions(cls, action, username, symbol, last_price, volume):

        cls.cur.execute("""INSERT INTO transactions(buy_sell, symbol, transact_price, quantity, user) 
                                VALUES(?,?,?,?,?)""",
                        (action, symbol, last_price, volume, username,))
        cls.conn.commit()

    @classmethod
    def update_balance(cls, username, delta):

        balance = cls.retrieve_balance(username)
        new_balance = balance + delta
        cls.cur.execute('UPDATE users SET balance = ? WHERE username = ?', (new_balance, username))
        cls.conn.commit()

    @classmethod
    def update_holdings(cls, username, symbol, volume):

        cls.cur.execute('SELECT quantity FROM stocks where user = ? AND symbol = ?', (username, symbol,))
        holding_vol = cls.cur.fetchone()

        if holding_vol is None:
            cls.cur.execute("""INSERT INTO stocks(symbol, quantity, user) 
                                            VALUES(?,?,?)""",
                            (symbol, volume, username,))
        else:
            new_vol = holding_vol[0] + volume
            if new_vol == 0:
                cls.cur.execute('DELETE FROM stocks WHERE user = ? AND symbol = ?', (new_vol, username, symbol,))
            else:
                cls.cur.execute('UPDATE stocks SET quantity = ? WHERE user = ? AND symbol = ?',
                                (new_vol, username, symbol,))
        cls.conn.commit()

    @classmethod
    def fetch_portfolio(cls, username):
        query = "SELECT symbol, quantity FROM stocks WHERE user = '{}'".format(username)
        return psql.read_sql_query(query, cls.conn)


    @classmethod
    def close_conn(cls):
        cls.cur.close()
        cls.conn.close()



#create_users()
#print(ORM.verify_identity('kapil', 'blah'))
#print(ORM.username_available('abc'))
#ORM.create_users('uk', 'blah', 'Uday')
#print(ORM.retrieve_balance('kapil'))
#ORM.update_transactions('long', 'kapil', 'GOOG', 1000, 10)
#ORM.update_balance('kapil', -1000)
#print(ORM.retrieve_balance('kapil'))
#ORM.update_holdings('long', 'kapil', 'GOOG', 1000, 20)
#print(ORM.fetch_portfolio('kapil'))