import sqlite3

conn = sqlite3.connect("Players.sqlite3")

cur = conn.cursor()

query = """
create table player (
plyid varchar(5) PRIMARY KEY,
plyname varchar(50) not null,
sport varchar(30) not null, 
achievement varchar(50) not null
)
"""

cur.execute(query)

conn.close()
