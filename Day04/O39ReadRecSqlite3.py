

import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect("Players.sqlite3")

cur = conn.cursor()

cur.execute("select * from player")

# for row in cur.fetchall():
#     print(row)

prtyTbl = from_db_cursor(cur)

conn.close()
prtyTbl.align['plyname'] = "l"
prtyTbl.align['sport'] = "l"
prtyTbl.align['achievement'] = "r"

print(prtyTbl)

