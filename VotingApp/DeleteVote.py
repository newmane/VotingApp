import psycopg2

conn = psycopg2.connect(
        database='database_name',
        user='username',
        password='password',
        host='host',
        port='port'
      )

cur = conn.cursor()

number = input("Enter number of the vote you want to delete: ")
query = "DELETE FROM VOTERS WHERE NUMBER = %s"
cur.execute(query, (number,)) 

conn.commit()
conn.close()

