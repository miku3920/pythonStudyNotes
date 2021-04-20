from selenium import webdriver
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe',chrome_options=option)
driver.get('https://www.ruten.com.tw/')

elem = driver.find_element_by_id("keyword")
elem.clear()
elem.send_keys("miku3920")
elem.send_keys(Keys.RETURN)
# driver.close()
