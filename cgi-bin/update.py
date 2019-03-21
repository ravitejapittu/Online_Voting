import sqlite3,cgi
print("Content-type:text/html \r\n\r\n")

form=cgi.FieldStorage()
party=form.getvalue("partyName")
print(party)
try:
	conn=sqlite3.connect("election.db")
	cur=conn.cursor()
	sql="select party_name from electers where party_name='"+party+"'"
	cur.execute(sql)
	for row in cur.fetchall():
		data=row[0]
	if party==data:
		query="update electers set count=count+1 where party_name='"+data+"'"
		print(query)
		cur.execute(query)
		conn.commit()
		print("<p onload='window.location.assign(../vote.html)'></p>")
except Exception as e:
	print(e)

# if party=="CONGRESS":
# 	#print(party)
# 	try:
# 		conn=sqlite3.connect("election.db")
# 		cur=conn.cursor()
# 		sql="update electers set count=count+1 where party_name='"+party+"'"
# 		print(sql)
# 		cur.execute(sql)
# 		conn.commit()
# 	except Exception as e:
# 		print(e)
# elif party=="BJP":
# 	#print(party)
# 	try:
# 		conn=sqlite3.connect("election.db")
# 		cur=conn.cursor()
# 		sql="update electers set count=count+1 where party_name='"+party+"'"
# 		print(sql)
# 		cur.execute(sql)
# 		conn.commit()
# 	except Exception as e:
# 		print(e)

# try:
# 	form=cgi.FieldStorage()
# 	party=form.getvalue("CONGRESS")
# 	conn=sqlite3.connect("election.db")
# 	c=conn.cursor()
# 	i=1
# 	sql="update electors set count+=1 where party_name='"+party+"'"
# 	print(sql)
# 	c.execute(sql)
# 	conn.commit()
# except Exception as e:
# 	print(e)
# try:
# 	c.execute(sql)
# except Exception as e:
# 	print(e)
# else:
# 	for record in cur:
# 		pass
# finally:
# 	conn.commit()
# 	print("success")
#     c.close()
#     conn.close()