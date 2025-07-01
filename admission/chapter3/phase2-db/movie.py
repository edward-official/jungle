import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
jungleDB = client.dbjungle


def convertToMinutes(time):
    #FORMAT DEPENDENT: "2h 16m"
    time = time.replace("h", "").replace("m", "")
    hours, minutes = time.split(" ")
    hours = int(hours)
    minutes = int(minutes)
    result = hours * 60 + minutes
    return result

def insertMovies():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.select('.ipc-page-grid__item--span-2 > .ipc-metadata-list--base > li')
    for movie in movies:
        movieTitle = movie.select_one('.ipc-title-link-wrapper > h3')
        if not movieTitle:
            continue

        title = movieTitle.text.split(". ", 1)[1]
        released_year = int(movie.select_one('.cli-title-metadata-item:nth-child(1)').text)
        running_time = movie.select_one('.cli-title-metadata-item:nth-child(2)').text
        running_time_minutes = convertToMinutes(running_time)
        pg_level = movie.select_one('.cli-title-metadata-item:nth-child(3)').text

        doc = { 
            'title': title,
            'released_year': released_year,
            'running_time': running_time_minutes,
            'pg_level': pg_level,
        }
        jungleDB.movies.insert_one(doc)
        print('완료: ', title, released_year, running_time, pg_level)


if __name__ == '__main__':
    jungleDB.movies.drop()
    insertMovies()