import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient("localhost", 27017)
database = mongo.football

@app.route('/')
def home():
  return render_template('index.html')

@app.route("/save", methods=["POST"])
def save():
  playerName = request.form["playerNameGive"]
  uniformNumber = request.form["uniformNumberGive"]
  player = {"player_name": playerName, "uniform_number": uniformNumber}
  players = list(database.players.find({"uniform_number": uniformNumber}))
  if len(players)==0:
    database.players.insert_one(player)
  else:
    print("player information already exists")
  return jsonify({'result': 'success'})

@app.route("/api/players")
def apiPlayers():
  players = list(database.players.find({}, {"_id":False}))
  return jsonify({"result": "success", "players": players})

if __name__ == '__main__':
  app.run('0.0.0.0',port=5001,debug=True)