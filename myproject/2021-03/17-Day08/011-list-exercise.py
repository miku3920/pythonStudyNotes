scoreList = []
while True:
    score = input('輸入數學成績(q離開): ')
    if score == 'q':
        break

    try:
        score = int(score)
    except:
        print('  輸入錯誤!!')
        continue

    if score > 100 or score < 0:
        print('  輸入錯誤!!')
        continue

    scoreList.append(score)

print(scoreList)
passList = [x for x in scoreList if x >= 60]
print(passList)
addPointsList = [x+10 for x in scoreList if x < 60]
print(addPointsList)
sortList = addPointsList.copy()
sortList.sort()
print(sortList)
indexList = [scoreList.index(x-10) for x in sortList]
print(indexList)
