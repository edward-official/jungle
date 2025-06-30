import requests # requests 라이브러리 설치 필요

response = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
json = response.json()

towns = json['RealtimeCityAir']['row']
for town in towns:
  if town['IDEX_MVL'] < 60:
    print (town['MSRSTE_NM'], town['IDEX_MVL'])
