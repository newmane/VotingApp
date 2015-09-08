from flask import Flask, request, redirect
from bandwidth_sdk import Client, Message, MessageEvent, Event
Client('CATAPULT_USER_ID', 'CATAPULT_API_TOKEN', 'CATAPULT_API_SECRET')

import psycopg2

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond():
  event = Event.create(**request.json)
  text = event.text
  remotenum = event.from_
  numbers = []
  #numbers is a list of numbers allowed to vote
  numbers.append('+12345678910')
  numbers.append('+11098765432')
  index = 0
  for i in range(len(numbers)):
    if event.from_ == numbers[i]:
      allowed = 0
      index = i
  if allowed == 0:
    if text == "yes" or text == "Yes":
      message = "Welcoming to TextYourVote. If you are ready to get started type 'Menu'"
      return respond(event, message)
    if text == "Menu":
      message =  "Menu - Type 1 to vote, and 2 to see platforms."
      return respond(event, message)
    if text == "1":
      message = "Text 'Ady' to vote for Ady or 'James' to vote for James."
      return respond(event, message)
    if text == "2":
      message =  "Text 'more Ady' to learn more about Ady's platform or 'more James' to learn more about James' platform."
      return respond(event, message)
    if text == "more Ady" or text == "More Ady":
      message = "Ady wants to rule the world."
      return respond(event, message)
    if text == "more James" or text == "More James":
      message = "James promises snickers to all who vote for him."
      return respond(event, message)
    if text == "Ady" or text == "James":
      allowed = check(remotenum)
      if allowed == 0:
        addtodatabase(remotenum, text)
        message = "Thanks for voting!"
        return respond(event, message)
      else: 
        message = "You have already voted sorry."
        return respond(event, message)
    else:
      message = "Sorry I do not understand that command."
      return respond(event, message)
  else:
      message = "You do not have permission to use this."
      return respond(event, message)

def respond(event, message):
  mynum = event.to 
  remotenum = event.from_
  response = Message.send(mynum, remotenum, message) 
  return response


def addtodatabase(remotenum, text):
  conn = psycopg2.connect(
        database='database_name',
        user='username',
        password='password',
        host='host',
        port='port'
      )
  cur = conn.cursor()
  cur.execute("INSERT INTO VOTERS (NUMBER, VOTE) " \
              "VALUES (%s, %s)",
              (remotenum, text))
  conn.commit()
  conn.close()
  return "Table changed"
    
def check(remotenum):
  conn = psycopg2.connect(
        database='database_name',
        user='username',
        password='password',
        host='host',
        port='port'
      )
  cur = conn.cursor()
  cur.execute("SELECT NUMBER, VOTE from VOTERS")
  rows = cur.fetchall()
  check = 0
  for r in rows:
    if remotenum == r[0]:
      check = 1
  conn.commit()
  conn.close()
  return check


if __name__ == "__main__":
    app.run(debug=True)
  