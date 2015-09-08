import psycopg2

conn = psycopg2.connect(
    conn = psycopg2.connect(
        database='database_name',
        user='username',
        password='password',
        host='host',
        port='port'
      )
)

cur = conn.cursor()
cur.execute("""CREATE TABLE VOTERS 
       (NUMBER TEXT, VOTE TEXT)""")
       
conn.commit()
conn.close()