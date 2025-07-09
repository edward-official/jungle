import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient("localhost", 27017)
database = mongo.jungle
collection = database.movies

arrangeMethod = "releasedYearDescending"
"""
default: database order (desecnding)
likes: descending
releasedYear: ascending
"""

@app.route('/', methods=["GET"])
def home():
  return render_template('index.html')

@app.route("/listup", methods=["GET"])
def listup():
  movies = list(collection.find())
  for movie in movies:
    movie["_id"] = str(movie["_id"])
  return jsonify({"result": "success", "movies": movies})


if __name__ == '__main__':
  app.run('0.0.0.0',port=5001,debug=True)