import json

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+'\\'

with open(path+'u-bike.json', 'r', encoding="utf-8") as fp:
    data = json.load(fp)
    # print(data["retVal"]["2001"]["sna"])

    retVal = data["retVal"]
    for key in retVal:
        info = retVal[key]
        if int(info["sbi"]) < int(info["tot"])//2: # 可借數量小於一半
            print("站名: ", info["sna"],
                  "所有數量: ", info["tot"],
                  "可借數量: ", info["sbi"])
