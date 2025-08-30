from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)
mongoDB = MongoClient('localhost', 27017)
database = mongoDB.openPL


@app.route('/')
def home():
  return render_template('login.html')


@app.route("/login", methods=["POST"])
def login():
  userId = request.form["userId"]
  password = request.form["password"]

  drawnTuple = database.users.find_one({"userId": userId})
  isRequestAccepted = True
  if drawnTuple==None:
    isRequestAccepted = False
    print("no tuple found")
  elif drawnTuple["password"]!=password:
    isRequestAccepted = False
    print("password incorrect")

  return jsonify({"result": "success", "isRequestAccepted": isRequestAccepted})


@app.route("/signup", methods=["POST"])
def signup():
  print("🚨 check point 1")
  userId = request.form["userId"]
  print("🚨 check point 2")
  drawnTuple = database.users.find_one({"userId": userId})
  if drawnTuple!=None:
    print("🚨 case 1")
    return jsonify({"isRequestAccepted": False, "reason": "redundancy"})

  password1 = request.form["password1"]
  password2 = request.form["password2"]
  if password1!=password2:
    print("🚨 case 2")
    return jsonify({"isRequestAccepted": False, "reason": "passwords do not match"})
  
  user = {"userId": userId, "password": password1}
  database.users.insert_one(user)
  print("🚨 case 3")
  return jsonify({"isRequestAccepted": True})


@app.route("/questions", methods=["GET"])
def questions():
  print("🚨 rendering questions.html")
  return render_template("questions.html")


if __name__ == '__main__':
  app.run('0.0.0.0', port=5001, debug=True)
