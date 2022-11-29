#!C:\Users\user\AppData\Local\Programs\Python\Python39\python.exe
print()
print ("""
    <TITLE>CGI script ! Python</TITLE>
    
""")

import blockchainLib as bl
import cgi
import mysql.connector

form = cgi.FieldStorage()
searchterm =  form.getvalue('field_1')
#print(searchterm)
if __name__ == "__main__":

		bl.initBlock()
		bl.addNewBlock(searchterm)
		#bl.addNewBlock("Vijaya")
		d=bl.getAllBlocks()
		#print(d)
conn = mysql.connector.connect(host="localhost",user="root",password="",database='sis')
mycursor = conn.cursor()
sql = "UPDATE student SET hashcode =%s WHERE EnrollmentNumber =%s"
#print("record inserted.")

val=(d,searchterm)
#print("inserted.")

mycursor.execute(sql,val)

conn.commit()

print("<h1>Hash added successfully</h1>")
#print("hello")
