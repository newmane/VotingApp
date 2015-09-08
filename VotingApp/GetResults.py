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

cur.execute("SELECT NUMBER, VOTE from VOTERS")

rows = cur.fetchall()

adycount = 0
jamescount = 0
for r in rows:
    if r[1] == "Ady":
      adycount = adycount + 1
    if r[1] == "James":
      jamescount = jamescount + 1
      
      
import plotly.plotly as py
from plotly.graph_objs import *
data =([
    Bar(
    x = ['Ady', 'James'],
    y = [adycount, jamescount]
    )
  ])
plot_url = py.plot(data, filename= 'Votes')

      
print ("Ady: " + str(adycount))
print ("James: " + str(jamescount))

conn.commit()
conn.close()