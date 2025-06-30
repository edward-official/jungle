import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

def townsOfDecentFineDust(criterion):
  towns = rjson['RealtimeCityAir']['row']
  result = ""
  for town in towns:
    if town["IDEX_MVL"]<criterion:
      result += town['MSRSTE_NM'] + ": " + str(town['IDEX_MVL']) + "\n"
  return result
print(townsOfDecentFineDust(50))