import sqlite3 as sq

conn = sq.connect("cms.db")  #create database
print("database created")

csr=conn.cursor();      #moving the sursor to database

"""
csr.execute("CREATE TABLE emp1 (eid INTEGER PRIMARY KEY, ename TEXT, salary INTEGER(10,2))")  #sql query
print("Table created")
"""
csr.execute("INSERT INTO emp1 VALUES(101, 'Neelima', 10000)")
csr.execute("INSERT INTO emp1 VALUES(102, 'Raj', 50000)")
csr.execute("INSERT INTO emp1 VALUES(103, 'Raj', 50000)")
print("data inserted")

empRec=csr.execute("SELECT * FROM emp1")
print(empRec.fetchall())

ed=102
usal= 70000
csr.execute("UPDATE emp1 SET salary=? WHERE eid=?", (usal, ed))
print("details updated")

empRec=csr.execute("SELECT * FROM emp1 WHERE eid=102")
print(empRec.fetchall())
