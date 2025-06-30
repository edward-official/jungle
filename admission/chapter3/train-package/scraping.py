import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('.cli-parent')

print("--------------------------------")
print(len(movies)) # 가져온 영화 개수
print("--------------------------------")
print(movies[0]) # 첫번째 영화 요소
print("--------------------------------")
print(movies[0].select_one('h3')) # 첫번째 영화 요소의 h3 요소
print("--------------------------------")
print(movies[0].select_one('h3').text) # 첫번째 영화 제목
print("--------------------------------")

# movies(li들)의 반복문을 돌리기
for movie in movies:
  # movie 안에 h3 가 있으면,
  # (조건을 만족하는 첫 번째 요소, 없으면 None을 반환한다.)
  h3_element = movie.select_one('h3')
  print(h3_element.text)