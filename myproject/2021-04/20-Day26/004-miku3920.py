from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

option = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
driver.get('https://miku3920.net/')

wait_a = WebDriverWait(driver, 10)
element_a = EC.element_to_be_clickable((By.ID, 'text1'))
elem_a = wait_a.until(element_a)
elem_a.clear()
elem_a.send_keys("miku3920")

wait_b = WebDriverWait(driver, 10)
element_b = EC.element_to_be_clickable((By.ID, 'btn1'))
elem_b = wait_b.until(element_b)
elem_b.click()
sleep(5)

html = driver.page_source
print(html)
sleep(5)
driver.close()
