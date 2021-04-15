import requests
from bs4 import BeautifulSoup

text1="""
<head>
    <title>miku3920</title>
</head>
<body>
    <p class="title"><b>The test</b></p>
    <a class="redcolor" href="http://miku3920.net?p=1" id="link1">test1</a>
    <a class="bluecolor" href="http://miku3920.net?p=2" id="link2">test2</a>
    <a class="redcolor"  href="http://miku3920.net?p=3" id="link3">test3</a>
</body>
"""
soup=BeautifulSoup(text1, "html.parser")

print('-------- title --------')

print(soup.title)
# <title>miku3920</title>
print(soup.title.name)
# title
print(soup.title.string)
# miku3920
print(soup.title.parent.name)
# head

print('-------- a --------')

print(soup.a)
# <a class="redcolor" href="http://miku3920.net?p=1" id="link1">test1</a>
print(soup.a.get('href'))
# http://miku3920.net?p=1
print(soup.a.string)
# test1

print('-------- select --------')

print(soup.select('.bluecolor')[0].string)
# test2
print(soup.select('#link2')[0].string)
# test2
print(soup.select('#link3')[0].string)
# test3
print(soup.select('a')[0].string)
# test1

print('-------- find_all --------')

print(soup.find_all('a')[0].get('href'))
# http://miku3920.net?p=1
print(soup.find_all('a')[0].string)
# test1