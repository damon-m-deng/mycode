#!/usr/bin/env python3

# https://docs.python.org/3/library/sqlite3.html

import sqlite3

# create a connection object test.db
conn=sqlite3.connect('test.db')
print('Opened database successfully.')

# insert some sql data
# conn.execute: do something. CREATE, SELECT, etc
# BEST PRACTICE: docstrings for SQL strings '''SQL''';
conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
        (
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL
        );''')
print('Table created successfully.')
conn.close()
