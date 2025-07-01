import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
jungleDB = client.dbjungle

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select("li.ipc-metadata-list-summary-item")


def scrapReleasedYear(targetName):
  for movie in movies:
    name = movie.select_one("h3.ipc-title__text").text
    releasedYear = movie.select_one("span.JTbpG:nth-child(1)").text
    # print(name + " (" + releasedYear + ")")
    if targetName in name:
      return int(releasedYear)
# print(scrapReleasedYear("The Two Towers"))

def findReleasedYear(targetName):
  targetMovie = jungleDB.movies.find_one({"title": targetName})
  return targetMovie["released_year"]
# print(findReleasedYear("포레스트 검프"))


def scrapMovieTitles(targetYear):
  movieTitles = []
  for movie in movies:
    name = movie.select_one("h3.ipc-title__text").text.split(". ")[1]
    releasedYear = int(movie.select_one("span.JTbpG:nth-child(1)").text)
    print(name + " (" + str(releasedYear) + ")")
    if targetYear == releasedYear:
      movieTitles.append(name)
  return movieTitles
# print(scrapMovieTitles(scrapReleasedYear("The Two Towers")))
# print(scrapMovieTitles(1994))

def findMovieTitles(targetYear):
  targetMovies = jungleDB.movies.find({"released_year": targetYear})
  targetTitles = []
  for movie in targetMovies:
    targetTitles.append(movie["title"])
  return targetTitles
# print(findMovieTitles(1994))


def scrapParsedName(targetName):
  for movie in movies:
    name = movie.select_one("h3.ipc-title__text").text
    if targetName in name:
      return name.split(". ")[1]
def updateReleasedYear(targetName, targetYear):
  properName = scrapParsedName(targetName)
  jungleDB.movies.update_one({"title": properName}, {"$set": {"released_year": targetYear}})
# updateReleasedYear("The Lord of the Rings: The Two Towers", 0)

