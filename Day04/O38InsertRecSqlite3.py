
import sqlite3

conn = sqlite3.connect("Players.sqlite3")

cur = conn.cursor()

FL = open("query.txt", "r")

for qry in FL.readlines():
    cur.execute(qry)

conn.commit()
conn.close()
FL.close()
