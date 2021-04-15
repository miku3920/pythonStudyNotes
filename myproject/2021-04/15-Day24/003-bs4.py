import requests
import bs4
from bs4 import BeautifulSoup

text1 = """
<head>
    <title>miku3920</title>
</head>
<body>
    <div>
        Fruit
        <h1 class="d1"> 水果</h1>
    	<ul class="d2">
        	<li> 蘋果 </li>
        	<li> 橘子 </li>
        </ul>

        Food
        <h1 class="d3"> 餐點</h1>
    	<ul class="d4">
        	<li> 魯肉販 </li>
        	<li> 雞排 </li>
        </ul>
    </div>
</body>
"""

soup = BeautifulSoup(text1, "html.parser")

print(soup.select('ul')[1].select('li')[0].string)
# 魯肉販

items = soup.select('div')[0].contents
for item in items:
    if type(item) is bs4.element.NavigableString:
        string = item.string.strip()
        if string:
            print(string)
# Fruit
# Food