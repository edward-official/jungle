import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from flask.json.provider import JSONProvider

app = Flask(__name__)
mongo = MongoClient("localhost", 27017)
database = mongo.jungle
collection = database.movies

@app.route('/', methods=["GET"])
def home():
  return render_template('index.html')

@app.route("/listup", methods=["GET"])
def listup():
  isLikeOrderPrior = request.args.get("isLikeOrderPrior")
  yearOrder = int(request.args.get("yearOrder"))
  likeOrder = int(request.args.get("likeOrder"))
  movies = []
  if isLikeOrderPrior=="true":
    movies = list(collection.find().sort([("likes", likeOrder), ("releasedYear", yearOrder)]))
  else:
    movies = list(collection.find().sort([("releasedYear", yearOrder), ("likes", likeOrder)]))
  for movie in movies:
    movie["_id"] = str(movie["_id"])
  return jsonify({"result": "success", "movies": movies})

@app.route("/like", methods=["POST"])
def like():
  movieID = request.form["movieID"]
  selectedMovie = collection.find_one({"_id": ObjectId(movieID)}, {})
  updatedLike = selectedMovie["likes"] + 1
  print(updatedLike)
  collection.update_one({"_id": ObjectId(movieID)}, {"$set": {"likes": updatedLike}})
  return jsonify({"result": "success"})

@app.route("/hide", methods=["POST"])
def hide():
  movieID = request.form["movieID"]
  # print("movieID: " + movieID)
  collection.update_one({"_id": ObjectId(movieID)}, {"$set": {"hidden": True}})
  return jsonify({"result": "success"})

@app.route("/unhide", methods=["POST"])
def unhide():
  movieID = request.form["movieID"]
  collection.update_one({"_id": ObjectId(movieID)}, {"$set": {"hidden": False}})
  return jsonify({"result": "success"})

@app.route("/delete", methods=["POST"])
def delete():
  movieID = request.form["movieID"]
  collection.delete_one({"_id": ObjectId(movieID)})
  return jsonify({"result": "success"})


if __name__ == '__main__':
  app.run('0.0.0.0',port=5001,debug=True)