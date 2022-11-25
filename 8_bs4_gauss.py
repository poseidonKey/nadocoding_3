import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url=url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
cartoons = soup.find_all("td", attrs={"class": "title"})
# title=cartoons[0].a.text
# print(title)
# link=cartoons[0].a["href"]
# print(link)

for cartoon in cartoons:
    title = cartoon.a.text
    link = "https://comic.naver.com"+cartoon.a["href"]
    print(title, link)
