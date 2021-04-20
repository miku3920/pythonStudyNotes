from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# download chromedriver
# pip install selenium

option = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe',chrome_options=option)
driver.get('http://www.python.org')


elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("miku3920")
elem.send_keys(Keys.RETURN)
# driver.close()
