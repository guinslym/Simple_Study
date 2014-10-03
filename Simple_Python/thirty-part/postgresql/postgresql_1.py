import psycopg2
conn = psycopg2.connect("user=postgres dbname=test")
cur = conn.cursor()
cur.execute("select * from blog_author")
rows = cur.fetchall()
for i in rows:
	print i
cur.close()
conn.commit()
conn.close()