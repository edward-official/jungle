import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get("https://en.wikipedia.org/wiki/Krafton", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tableOfContents = soup.select(".vector-toc-list-item span:nth-child(2)")
for content in tableOfContents:
  print(content.text)

print(soup)