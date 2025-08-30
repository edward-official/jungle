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
  isRequestAccepted = True
  if drawnTuple==None:
    isRequestAccepted = False
    print("no tuple found")
  elif drawnTuple["pw"]!=pw:
    isRequestAccepted = False
    print("password incorrect")

  return jsonify({"result": "success", "isRequestAccepted": isRequestAccepted})


@app.route("/signup", methods=["POST"])
def signup():
  id = request.form["id"]
  drawnTuple = database.users.find_one({"id": id})
  if drawnTuple!=None:
    # print("case 1")
    return jsonify({"isRequestAccepted": False, "reason": "redundancy"})

  pw1 = request.form["pw1"]
  pw2 = request.form["pw2"]
  if pw1!=pw2:
    # print("case 2")
    return jsonify({"isRequestAccepted": False, "reason": "password"})
  
  user = {"id": id, "pw": pw1}
  database.users.insert_one(user)
  # print("case 3")
  return jsonify({"isRequestAccepted": True})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5001, debug=True)
