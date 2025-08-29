from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)
mongoDB = MongoClient('localhost', 27017)
database = mongoDB.openPL


@app.route('/')
def home():
  return render_template('language.html')

@app.route("/login", methods=["POST"])
def login():
  id = request.form["id"]
  pw = request.form["pw"]

  drawnTuple = database.users.find_one({"id": id})
  isAuthenticated = True
  if drawnTuple==None:
    isAuthenticated = False
    print("no tuple found")
  elif drawnTuple["pw"]!=pw:
    isAuthenticated = False
    print("password incorrect")

  return jsonify({"result": "success", "isAuthenticated": isAuthenticated})

@app.route("/singup", methods=["POST"])
def signup():
  id = request.form["id"]
  pw = request.form["pw"]

  user = {"id": id, "pw": pw}
  database.users.insert_one(user)

  return jsonify({"result": "success"})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5001, debug=True)
