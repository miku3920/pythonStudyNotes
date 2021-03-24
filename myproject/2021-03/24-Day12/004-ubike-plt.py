import matplotlib.pyplot as plt
import json

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+'\\'

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

nameList = []
existList = []
vacancyList = []
with open(path+'u-bike.json', 'r', encoding="utf-8") as fp:
    data = json.load(fp)
    # print(data["retVal"]["2001"]["sna"])

    items = data["retVal"]
    for key in items:
        info = items[key]

        nameList.append(info["sna"])
        existList.append(int(info["sbi"]))
        vacancyList.append(int(info["tot"])-int(info["sbi"]))

        # if int(info["sbi"]) < int(info["tot"])//2:  # 可借數量小於一半
        #     print("站名: ", info["sna"],
        #           "所有數量: ", info["tot"],
        #           "可借數量: ", info["sbi"])

start=15
end=20

fig, ax = plt.subplots()
ax.bar(nameList[start:end], existList[start:end], label='車子數量')
ax.bar(nameList[start:end], vacancyList[start:end], bottom=existList[start:end], label='空位數量')
ax.set_title('u-bike')
ax.legend()
plt.show()
