from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(by=By.CLASS_NAME, value="link_login")
elem.click()
