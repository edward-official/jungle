import requests # requests 라이브러리 설치 필요

response = requests.get("https://www.naver.com/")
# print(response.text)
# print(response.status_code)
print(response.json())