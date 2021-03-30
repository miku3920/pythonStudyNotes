import csv

with open('opendata10706L010.csv', 'r', newline='', encoding='utf-8') as fp:
    read = csv.reader(fp, delimiter=',')
    englishHeader = next(read)
    print(englishHeader)
    chineseHeader = next(read)
    print(chineseHeader)
    for row in read:
        if row[2] == '陳':
            print('統計年月:', row[0], '區域別:', row[1], '姓氏:',
                  row[2], '性別:', row[3], '人口數:', row[4])

fp.close()
