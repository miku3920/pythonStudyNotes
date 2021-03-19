import csv

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+"\\"

with open(path+'消費紀錄.csv', 'r', newline='', encoding='utf-8') as fp:
    read = csv.reader(fp, delimiter=',')
    header = next(read)
    print(header)
    for row in read:
        print(row)

fp.close()