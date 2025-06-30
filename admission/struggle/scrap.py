import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('.cli-parent')

# 첫번째 영화 요소 추출
movie = movies[0]

# 제목 요소 추출
h3_element = movie.select_one('h3')
print(h3_element.text)

# 개봉 연도 요소 추출
year_element = movie.select('.cli-title-metadata-item')[0]
print(year_element.text)

# 상영 시간 요소 추출
runtime_element = movie.select('.cli-title-metadata-item')[1]
print(runtime_element.text)

# 등급 요소 추출
rating_element = movie.select('.cli-title-metadata-item')[2]
print(rating_element.text)
