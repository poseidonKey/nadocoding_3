import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res = requests.get(url=url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
print(res.text)
items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).text)
for item in items:
    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("광고 제품 제외!!")
        continue
    name = item.find("div", attrs={"class": "name"}).text
    # Apple 상품 제외
    if "Apple" in name:
        print("< Apple > 상품 제외")
        continue

    price = item.find(
        "strong", attrs={"class": "price-value"}).get_text()  # 가격
    # 리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})  # 평점
    if rate:
        rate = rate.get_text()
    else:
        # rate = "평점 없음"
        print("<평점 없는 상품 제외>")
        continue
    rate_count = item.find(  # 평점 합계
        "span", attrs={"class": "rating-total-count"}).get_text()  # ex : (26)
    if rate_count:
        rate_count = rate_count.get_text()
        rate_count = rate_count[1:-1]
    else:
        # rate_count = "합계 없음"
        print("<평점 수 없는 상품 제외>")
        continue

    if float(rate) >= 4.5 and int(rate_count) >= 50:
        print("==========================================")
        print(name, price, rate, rate_count)
