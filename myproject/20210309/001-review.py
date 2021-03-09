english = [90, 80, 90, 100]

topScore = 0
topIndex =  0
for i in range(len(english)):
    # 印出每一個
    print(english[i])
    if english[i] > topScore:
        topScore = english[i]
        topIndex = i
    if english[i] < 85:
        english[i] = english[i] + 5

# 印出最高分
print("topScore =",topScore)
# 印出最高分的同學
print("topIndex =",topIndex)
# 將 85 分以下的加五分
print(english)
