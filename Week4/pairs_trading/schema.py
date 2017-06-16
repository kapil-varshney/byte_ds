#!/usr/bin/env python3

import sqlite3


conn = sqlite3.connect("pairs_trading.db")
cur = conn.cursor()

cur.execute("""
            CREATE TABLE microsoft(
            LastPrice REAL,
            Change REAL,
            ChangePercent REAL,
            Timestamp DATETIME,
            MSDate INTEGER,
            MarketCap INTEGER,
            Volume INTEGER,
            ChangeYTD REAL,
            ChangePercentYTD REAL,
            High REAL,
            Low REAL,
            Open REAL
            );
            """)

cur.execute("""
            CREATE TABLE google(
            LastPrice REAL,
            Change REAL,
            ChangePercent REAL,
            Timestamp DATETIME,
            MSDate INTEGER,
            MarketCap INTEGER,
            Volume INTEGER,
            ChangeYTD REAL,
            ChangePercentYTD REAL,
            High REAL,
            Low REAL,
            Open REAL
            );
            """)

conn.commit()
cur.close()
conn.close()