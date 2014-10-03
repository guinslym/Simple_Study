import psycopg2
conn = psycopg2.connect("user=postgres dbname=test")
cur = conn.cursor()
cur.execute("insert into blog_author (id,first_name,last_name) values (%s,%s,%s)",(3,"Zhang","San"))
cur.execute("select * from blog_author")
rows = cur.fetchall()
for i in rows:
	print i
cur.close()
conn.commit()
conn.close()