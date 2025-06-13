


import sqlite3

conn = sqlite3.connect("Players.sqlite3")

cur = conn.cursor()

query = "delete from player where plyid = 'PlY333'"

cur.execute(query)
# if cur.rowcount == 0:
#     print("hello world")

conn.commit()
conn.close()
