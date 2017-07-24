import sqlite3


def update_transactions(action, username, symbol, last_price, volume):
    conn = sqlite3.connect("terminal_trading.db")
    cur = conn.cursor()
    cur.execute("""INSERT INTO transactions(buy_sell, symbol, transact_price, quantity, user) 
                            VALUES(?,?,?,?,?)""",
                (action, symbol, last_price, volume, username,))
    conn.commit()
    cur.close()
    conn.close()


update_transactions('long', 'kapil', 'GOOG', 1000, 10)
