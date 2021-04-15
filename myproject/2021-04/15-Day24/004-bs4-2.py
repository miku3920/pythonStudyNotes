import requests
from bs4 import BeautifulSoup
from os import path

if path.exists('req.html'):
    with open('req.html', 'r', encoding='utf-8') as f:
        html = f.read()
else:
    html = requests.get('http://www.powenko.com/wordpress/').text
    with open('req.html', 'w', encoding='utf-8') as f:
        f.write(html)

soup = BeautifulSoup(html, "html.parser")

items = soup.select('.largefeaturepowenA2')[0].select('.area')
for item in items:
    a = item.select('a')[1].contents[0]
    print(a.strip())
