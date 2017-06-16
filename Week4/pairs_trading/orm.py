#!/usr/bin/env python3

import sqlite3
import pandas.io.sql as psql


class ORM:

    conn = sqlite3.connect("pairs_trading.db")
    cur = conn.cursor()

    @classmethod
    def update_goog(cls, data):
        cls.cur.execute("INSERT INTO google VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (data['LastPrice'],
                         data['Change'],
                         data['ChangePercent'],
                         data['Timestamp'],
                         data['MSDate'],
                         data['MarketCap'],
                         data['Volume'],
                         data['ChangeYTD'],
                         data['ChangePercentYTD'],
                         data['High'],
                         data['Low'],
                         data['Open'],)
                        )

        cls.conn.commit()

    @classmethod
    def update_msft(cls, data):
        cls.cur.execute("INSERT INTO microsoft VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (data['LastPrice'],
                         data['Change'],
                         data['ChangePercent'],
                         data['Timestamp'],
                         data['MSDate'],
                         data['MarketCap'],
                         data['Volume'],
                         data['ChangeYTD'],
                         data['ChangePercentYTD'],
                         data['High'],
                         data['Low'],
                         data['Open'],)
                        )

        cls.conn.commit()

        # cur.execute("""
        #             CREATE TABLE microsoft(
        #             LastPrice REAL,
        #             Change REAL,
        #             ChangePercent REAL,
        #             Timestamp DATETIME,
        #             MSDate INTEGER,
        #             MarketCap INTEGER,
        #             Volume INTEGER,
        #             ChangeYTD REAL,
        #             ChangePercentYTD REAL,
        #             High REAL,
        #             Low REAL,
        #             Open REAL
        #             );
        #             """)

    @classmethod
    def retrieve_tables(cls, company_name):
        query = "SELECT * FROM {}".format(company_name)
        return psql.read_sql_query(query, cls.conn)

    @classmethod
    def close_conn(cls):
        cls.cur.close()
        cls.conn.close()
