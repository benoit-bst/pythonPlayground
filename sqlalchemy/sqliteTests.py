#!/usr/bin/python

import sqlite3

try:

  # Create db
  conn = sqlite3.connect('test_sqlite.db')

  cursor = conn.cursor()

  # create
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTEGER
  )
  """)
  conn.commit()

  # create
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS table2(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTEGER
  )
  """)
  conn.commit()

  # erase
  cursor.execute("""DROP TABLE table2""")
  conn.commit()

  # insert / set
  cursor.execute("""INSERT INTO users(name, age) VALUES(?, ?)""", ("olivier", 30))

  # get
  cursor.execute("""SELECT name, age FROM users""")
  user1 = cursor.fetchone()
  print(user1)

  # get
  cursor.execute("""SELECT id, name, age FROM users""")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

except sqlite3.OperationalError:
  print('Error creating db')

except Exception as e:
  print("Error")
  conn.roolback()

finally:
  # close db
  conn.close()