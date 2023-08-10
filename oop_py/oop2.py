import sqlite3

db = sqlite3.connect('database.db')

cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY,
date DATE,
description TEXT,
category TEXT,
price REAL)''')

db.commit()
db.close()