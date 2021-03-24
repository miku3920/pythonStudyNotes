import json
import sys
import urllib.request as httplib  # 3.x
import ssl

context = ssl._create_unverified_context()

url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=b3abedf0-aeae-4523-a804-6e807cbad589&rid=bf55b21a-2b7c-4ede-8048-f75420344aed"
req = httplib.Request(url)
reponse = httplib.urlopen(req, context=context)
contents = reponse.read()
data = json.loads(contents)
print(data)
length = len(data["datas"])   # 有幾台的資料
# 第二題：　顯示全部的bus
print("車號:", data["datas"][0]["BusID"], "營運狀態", data["datas"][0]["DutyStatus"],
      "行駛路線:", data["datas"][0]["RouteID"], "去返程:", data["datas"][0]["GoBack"],
      "緯度:", data["datas"][0]["Longitude"], "經度:", data["datas"][0]["Latitude"],
      "車速:", data["datas"][0]["Speed"])

# 第二題：　目前正在  spped>0
print("第二題：　目前正在  spped>0 ")
