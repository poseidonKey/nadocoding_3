# 네이버에서 코스피 시가총액 순위=> 시가총액 상위종목 더보기 클릭
# 상위 200개 자료 가져오기
# https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=2

import csv
import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
for page in range(1,5):
  res=requests.get(url+str(page))
  res.raise_for_status()
  soup=BeautifulSoup(res.text,"lxml")
  