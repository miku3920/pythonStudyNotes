import json
import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {
    'sensor': 'false',
    'address': '台北市信義區信義路五段7號',
    'key': '?????????????'
}
json0 = requests.get(url, params=params).content.decode("utf-8")
data = json.loads(json0)
lat = data["results"][0]["geometry"]["location"]["lat"]
lng = data["results"][0]["geometry"]["location"]["lng"]
print(lat, lng)
# 25.0338898 121.5650005
