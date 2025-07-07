from bson import ObjectId
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
from flask.json.provider import JSONProvider
import json
import sys

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbjungle

#####################################################################################
# 이 부분은 코드를 건드리지 말고 그냥 두세요. 코드를 이해하지 못해도 상관없는 부분입니다.
#
# ObjectId 타입으로 되어있는 _id 필드는 Flask 의 jsonify 호출시 문제가 된다.
# 이를 처리하기 위해서 기본 JsonEncoder 가 아닌 custom encoder 를 사용한다.
# Custom encoder 는 다른 부분은 모두 기본 encoder 에 동작을 위임하고 ObjectId 타입만 직접 처리한다.
class CustomJSONEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, ObjectId):
      return str(o)
    return json.JSONEncoder.default(self, o)

class CustomJSONProvider(JSONProvider):
  def dumps(self, obj, **kwargs):
    return json.dumps(obj, **kwargs, cls=CustomJSONEncoder)

  def loads(self, s, **kwargs):
    return json.loads(s, **kwargs)

# 위에 정의된 custom encoder 를 사용하게끔 설정한다.
app.json = CustomJSONProvider(app)
# 여기까지 이해 못해도 그냥 넘어갈 코드입니다.
#####################################################################################


#####
@app.route('/')
def home():
  return render_template('index.html')


@app.route('/api/list', methods=['GET'])
def show_movies():
  sortMode = request.args.get('sortMode', 'likes')
  if sortMode == "likes":
    movies = list(db.movies.find({'trashed': False}, {}).sort('likes', -1))
  elif sortMode == "viewers":
    movies = list(db.movies.find({'trashed': False}, {}).sort('viewers', -1))
  else:
    movies = list(db.movies.find({'trashed': False}, {})
                  .sort([('open_year', -1),('open_month', -1),('open_day', -1)]))
  return jsonify({'result': 'success', 'movies_list': movies})


@app.route("/api/trashMode", methods=["GET"])
def show_trashes():
  sortMode = request.args.get('sortMode', 'likes')
  if sortMode == "likes":
    movies = list(db.movies.find({'trashed': True}, {}).sort('likes', -1))
  elif sortMode == "viewers":
    movies = list(db.movies.find({'trashed': True}, {}).sort('viewers', -1))
  else:
    movies = list(db.movies.find({'trashed': True}, {})
                  .sort([('open_year', -1),('open_month', -1),('open_day', -1)]))
  return jsonify({'result': 'success', 'movies_list': movies})


@app.route('/api/like', methods=['POST'])
def like_movie():
  ID = request.form["_id"]
  movie = db.movies.find_one({"_id": ObjectId(ID), "trashed": False})
  if not movie:
    print("fail case 1")
    return jsonify({'result': 'failure'})
  new_likes = movie['likes'] + 1
  result = db.movies.update_one({'_id': movie['_id']}, {'$set': {'likes': new_likes}})
  if result.modified_count == 1:
    return jsonify({'result': 'success'})
  else:
    print("fail case 2")
    return jsonify({'result': 'failure'})
  

@app.route("/api/discard", methods=["POST"])
def discard():
  movieID = request.form["_id"]
  db.movies.update_one({"_id": ObjectId(movieID)}, {"$set" : {"trashed": True}})
  return jsonify({"result": "success"})


if __name__ == '__main__':
  print(sys.executable)
  app.run('0.0.0.0', port=5001, debug=True)
