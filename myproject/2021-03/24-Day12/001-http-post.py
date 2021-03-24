import sys
import urllib.parse
import urllib.request

url="http://miku3920.net/data.php"
values={'name':'powenko','password':123}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    contents = response.read().decode(response.headers.get_content_charset())
print(contents)