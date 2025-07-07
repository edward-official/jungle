import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://edward:jungle@13.209.35.88/', 27017)
db = client.dbjungle

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/memo', methods=['GET'])
def read_articles():
  result = list(db.articles.find({}, {'_id': 0}))
  return jsonify({'result': 'success', 'articles': result})


## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def post_article():
  url_receive = request.form['url_give']
  comment_receive = request.form['comment_give']

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(url_receive, headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')

  og_image = soup.select_one('meta[property="og:image"]')
  og_title = soup.select_one('meta[property="og:title"]')
  og_description = soup.select_one('meta[property="og:description"]')

  url_title = og_title['content']
  url_description = og_description['content']
  url_image = og_image['content']

  article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image, 'comment': comment_receive}

  db.articles.insert_one(article)
  return jsonify({'result': 'success'})


if __name__ == '__main__':
  app.run('0.0.0.0',port=5000,debug=True)