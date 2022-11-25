import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url=url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.text)
# print(soup.a["href"])  # 처음 발견되는 a 태그의 속성 중 href 내용 출력
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))

# print(soup.find("li",attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)
# print(rank1.a.text)
rank2 = rank1.next_sibling.next_sibling  # 줄 바꿈 때문에 두 번 처리. 계속 확인해 봐야 함.
# print(rank2.a.text)
# print(rank2.parent)
rank3 = rank2.find_next_sibling("li")  # 해당 되는 태그만 찾을 거다.
print(rank3.a.text)
rank4 = rank2.find_previous_sibling("li")
print(rank4.a.text)
print(rank1.find_next_siblings("li"))
webtoon = soup.find("a", text="나 혼자 만렙 뉴비-70화. 메두사 레이드(1)")
print(webtoon)
