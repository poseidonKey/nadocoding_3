from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url=url)
# 가는날 선택
browser.find_element(
    by=By.CLASS_NAME, value="searchBox_search__2KFn3").click()
    # by=By.CLASS_NAME, value="tabContent_option__2y4c6 select_Date__1aF7Y").click()
