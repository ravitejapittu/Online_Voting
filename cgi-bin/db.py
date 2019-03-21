import sqlite3,cgi
print("Content-type:text/html \r\n\r\n")

conn=sqlite3.connect("election.db")
c=conn.cursor()
sql="create table electers(id integer primary key autoincrement,party_name text unique,count integer)"
c.execute(sql)
conn.commit()
print("success")
c.close()
conn.close()