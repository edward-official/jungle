import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

mongo = MongoClient('localhost', 27017)
database = mongo.jungle
database.movies.drop()

movies = soup.select(".cli-children")
for movie in movies:
  title = movie.select_one(".ipc-title__text").text.split(". ")[1]
  releasedYear = movie.select_one(".cli-title-metadata-item:nth-child(1)").text
  runningTime = movie.select_one(".cli-title-metadata-item:nth-child(2)").text
  h = movie.select_one(".cli-title-metadata-item:nth-child(2)").text.split("h ")[0]
  m = movie.select_one(".cli-title-metadata-item:nth-child(2)").text.split("h ")[1].split("m")[0]
  rowData = {
    "title": title,
    "releasedYear": releasedYear,
    "runningTime": runningTime,
    "likes": 0,
    "hidden": False,
  }
  database.movies.insert_one(rowData)
