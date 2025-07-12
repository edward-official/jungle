from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
mongo = MongoClient('mongodb://edward:jungle@localhost:27017/')
database = mongo.dbjungle
collection = database.memos

@app.route('/', methods=["GET"])
def home():
  return render_template('index.html')

@app.route("/update/page", methods=["GET"])
def updatePage():
  memos = list(collection.find().sort("likes", -1))
  for memo in memos:
    memo["_id"] = str(memo["_id"])
  return jsonify({"result": "success", "memos": memos})

@app.route('/save/memo', methods=["POST"])
def saveMemo():
  title = request.form["title"]
  isTitleExisting = collection.find_one({"title": title})
  if isTitleExisting:
    return jsonify({"result": "ignored"})
  content = request.form["content"]
  if content == "":
    content = "default content"
  collection.insert_one({"title": title, "text": content, "likes": 0})
  return jsonify({"result": "success"})

@app.route("/button/edit", methods=["POST"])
def edit():
  memoID = request.form["memoID"]
  newTitle = request.form["title"]
  newText = request.form["text"]
  collection.update_one({"_id": ObjectId(memoID)}, {"$set": {"title": newTitle, "text": newText}})
  return jsonify({"result": "success"})

@app.route("/cancel/edit", methods=["GET"])
def cancelEdit():
  targetID = request.args["memoID"]
  memo = collection.find_one({"_id": ObjectId(targetID)})
  memo["_id"] = str(memo["_id"])
  return jsonify({"result": "success", "memo": memo})

@app.route("/button/delete", methods=["POST"])
def delete():
  memoID = request.form["memoID"]
  collection.delete_one({"_id": ObjectId(memoID)})
  return jsonify({"result": "success"})

@app.route("/button/like", methods=["POST"])
def like():
  memoID = request.form["memoID"]
  updatedLikes = collection.find_one({"_id": ObjectId(memoID)})["likes"] + 1
  collection.update_one({"_id": ObjectId(memoID)}, {"$set": {"likes": updatedLikes}})
  return jsonify({"result": "success"})

if __name__ == '__main__':
  app.run('0.0.0.0',port=5000,debug=True)