import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient("localhost", 27017)
database = mongo.football
collection = database.player

@app.route('/', methods=["GET"])
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0',port=5001,debug=True)