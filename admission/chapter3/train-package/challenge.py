import requests;
from bs4 import BeautifulSoup

headerArgument = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headerArgument)

soup = BeautifulSoup(data.text, "html.parser")
movies = soup.select(".ipc-metadata-list-summary-item")

for movie in movies:
  movieName = movie.select_one("h3").text
  spans = movie.select("span")
  movieReleasedYear = spans[1].text
  movieRunningTime = spans[2].text
  movieRating = spans[3].text
  result = f"{movieName}({movieReleasedYear}): {movieRunningTime}, {movieRating}"
  print(result)
