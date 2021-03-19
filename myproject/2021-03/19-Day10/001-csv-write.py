import csv

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+"\\"

with open(path+'消費紀錄.csv', 'w', newline='', encoding='utf-8') as fp:
    write = csv.writer(fp, delimiter=',')
    header = ["日期", "時間", "姓名", "品項", "總金額"]
    write.writerow(header)
    write.writerow(["2021-03-09", "08:40", "阿明", "XO", "510"])
    write.writerow(["2021-03-10", "16:46", "小美", "XX", "210"])
    write.writerow(["2021-03-11", "09:11", "昊哥", "OO", "350"])
    write.writerow(["2021-03-11", "12:07", "堂老大", "OX", "270"])

fp.close()
