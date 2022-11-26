# 네이버에서 코스피 시가총액 순위=> 시가총액 상위종목 더보기 클릭
# 상위 200개 자료 가져오기
# https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=2

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
filename = "시가총액1-200.csv"
# utf8로 하면 엑셀에서 한글 깨짐
f = open(file=filename, mode="w", encoding="utf-8-sig",
         newline="")  # newline은 그냥하면 한줄의 공백이 생기는 현상 제거
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split(
    "\t")
print(type(title))
writer.writerow(title)
for page in range(1, 5):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 의미 없는 데이터는 skip
            continue
        data = [column.text.strip() for column in columns]  # 불 필요한 내용 삭제
        # data=[column.text for column in columns]
        # print(data)
        writer.writerow(data)
