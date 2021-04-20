from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import bs4
from time import sleep

option = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)

sleep(2)

driver.get("https://m.facebook.com")
sleep(2)
# https://www.facebook.com/fukingstaff")
driver.get("https://m.facebook.com/wecarekhtw/")
normal_window = driver.current_window_handle
sleep(2)


# 移動到下一頁
for i in range(2):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(1)
sleep(5)

html = driver.page_source
# print(html)

soupA = BeautifulSoup(html, "html.parser")

p_items = soupA.select("article")[0].select("p")
for p in p_items: # 一個 article 裡有多個 p 段落
    items = p.contents
    for item in items: # 一個 p 段落裡有多個字串
        if type(item) is bs4.element.NavigableString:
            print(item.strip())
        else:
            print(item.text.strip())

sleep(5)
driver.close()
