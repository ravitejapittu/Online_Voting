import sqlite3,cgi
print("Content-type:text/html \r\n\r\n")


def dict_factory(cursor,row):
	d={}
	for idx,name,count col in enumerate(cursor.description):
		d[col[0]],d[col[1]],d[col[2]]=row[idx],row[name],row[count]
		print(d)
		# d[col[1]]=row[name]
		return d


conn=sqlite3.connect("election.db")
conn.row_factory=dict_factory
c=conn.cursor()
#sql="create table electers(id integer primary key autoincrement,party_name text unique,count integer)"
sql="select party_name from electers"
c.execute(sql)
results=c.fetchall()
print(results)

# with open(electers+'.json','a') as the_file:
# 	the_file.write(format(results).replace("u'","'").replace("'","\""))
# for c in c.fetchall():
# 	print(c[0],"<br>")

print("success")
c.close()
conn.close()