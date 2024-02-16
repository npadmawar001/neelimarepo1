"""
class Emp:
    eid=101
    ename="Radha"
    esal=5000

e1=Emp()        #default constructor : to create a object
print(e1.eid)
print(e1.ename)
print(e1.esal)

"""
import sqlite3 as sq
conn = sq.connect("cms.db")  #create database
print("database created")

csr=conn.cursor();  
#csr.execute("CREATE TABLE emp2 (eid INTEGER PRIMARY KEY, ename TEXT, salary INTEGER(10,2))")  #sql query
#print("Table created")


class Emp:
    eid=""
    ename=""
    esal=""

    def __init__(self, id, nm, sl):
        self.eid=id
        self.ename=nm
        self.esal=sl

    def displayEmployee(self):
        print("Hello" , self.ename , ". Your salary is: " , self.esal)


e1=Emp(105, "Krishna", 3000)
print(e1.ename)

e1.displayEmployee()                  #method of the class

csr.execute("INSERT INTO emp2 VALUES(?, ?, ?)", (e1.eid, e1.ename, e1.esal))


empRec=csr.execute("SELECT * FROM emp2")
print(empRec.fetchall())




