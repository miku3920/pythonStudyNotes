import matplotlib.pyplot as plt
import json

with open('垃圾車.json', 'r', encoding="utf-8") as fp:
    data = json.load(fp)
    items = data["result"]["records"]
    for i in range(len(items)):
        print(items[i]["清運點名稱"])
        print(items[i]["一般垃圾清運時間"])
        print()

# str1="星期一二四五六:17:10"
# if "四" in str1:
#     print("87")