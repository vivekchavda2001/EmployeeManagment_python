import sqlite3
class myconnect:
      
      def __init__(self):
            conn = sqlite3.connect('emp.db')
            conn.execute('''CREATE TABLE IF NOT EXISTS Employee  ( id integer primary key autoincrement, name text, email text, 
                     mobileno integer,employeetype text, experience integer, salary integer )''')
            conn.close()

      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            conn = sqlite3.connect('emp.db')
            conn.execute('insert into Employee values(NULL,?,?,?,?,?,?)',(ename,eemail,emob,etype,eexp,esalary))
            conn.commit()
            conn.close()

      def display(self):
            id = int(input("enter the emp id"))
            conn = sqlite3.connect('emp.db')
            data = conn.execute('select *from Employee where id = ?', (id,))           
            flag = 0
            for row in data:
                  flag = 1
                  print("=======================================================")
                  print("Name:", row[1])
                  print("Email:", row[2])
                  print("Mobile No:", row[3])
                  print("Employee Type:", row[4])
                  print("Experience:", row[5])
                  print("Salary:", row[6])
                  print("=======================================================")
            if flag == 0:
                  print("Invalid ID")
            conn.close()

      
