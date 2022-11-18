#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# the original table has AGE col, use cursor to get a subset of cols
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

print(cursor) # <sqlite3.Cursor object at 0x7f0c39cb0dc0>
print(type(cursor)) # <class 'sqlite3.Cursor'>

for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()

