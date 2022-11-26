import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url=url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
# cartoons = soup.find_all("td", attrs={"class": "title"})

# title=cartoons[0].a.text
# print(title)
# link=cartoons[0].a["href"]
# print(link)
# 만화 제목, 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.text
#     link = "https://comic.naver.com"+cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").text
    print(rate)
    total_rates += float(rate)
print("total grade :", total_rates)
print("average grade :", total_rates/len(cartoons))
