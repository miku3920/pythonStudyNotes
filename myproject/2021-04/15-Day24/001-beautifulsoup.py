# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

req=requests.get('http://www.powenko.com/wordpress/')
html=req.text
with open('req.html', 'w', encoding='utf-8') as f:
    f.write(html)

soup=BeautifulSoup(html, "html.parser")
print(soup.title.string)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))
t1=soup.find_all('a')
print(t1[0])

