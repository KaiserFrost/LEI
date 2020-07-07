import sqlite3

database = "dbtest.db"

conn = sqlite3.connect(database)
cur = conn.cursor()

cur.execute("SELECT cveID FROM ALLCVE")

rows = cur.fetchall()

print(rows)