import sqlite3

conn=sqlite3.connect('test.db')
print("Connection successful")

conn.execute("UPDATE COMPANY set SALARY=25000.00 WHERE ID=1")

conn.commit()
print("total number of rows updated:",conn.total_changes)

cursor=conn.execute('SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY')
for row in cursor:
    print("ID=", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
