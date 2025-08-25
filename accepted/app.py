from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)
mongoDB = MongoClient('localhost', 27017)
database = mongoDB.openPL


@app.route('/')
def home():
  return render_template('language.html')

@app.route("/login", methods=["GET"])
def login():
  id = request.args.get("id")
  print(id)
  return jsonify({"result": "success"})

@app.route("/singup", methods=["POST"])
def signup():
  id = request.form["id"]
  pw = request.form["pw"]

  user = {"id": id, "pw": pw}
  database.users.insert_one(user)

  return jsonify({"result": "success"})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5001, debug=True)
