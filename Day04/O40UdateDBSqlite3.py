


import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect("Players.sqlite3")

cur = conn.cursor()

query = "update player set plyname = 'Pusarla Venkata Sindhu' where plyid = 'PLY501'"

cur.execute(query)
if cur.rowcount == 0:
    print("hello world")

conn.commit()
conn.close()


# "delete from player where plyid = 'PLY323'