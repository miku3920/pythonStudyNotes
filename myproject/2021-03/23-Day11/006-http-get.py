import urllib.request as httplib

try:
    url="http://www.miku3920.net/"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        # contents=reponse.read().decode(reponse.headers.get_content_charset())
        contents=reponse.read().decode("UTF-8")
        print(contents)
except:
    print("error")   