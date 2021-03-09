score = [[90, 80, 90, 100],  # 英文
         [71, 72, 73, 74],  # 國文
         [81, 82, 83, 84]]  # 數學

subjectTopScore = [0, 0, 0]
topScore = 0
studentSumScore = [0, 0, 0, 0]
topScoreStudent = 0
for i in range(len(score)):
    for j in range(len(score[0])):
        if subjectTopScore[i] < score[i][j]:
            subjectTopScore[i] = score[i][j]
        if topScore < score[i][j]:
            topScore = score[i][j]
            topScoreStudent = j
        studentSumScore[j] += score[i][j]

print(score)                                # 印出每一個
print("subjectTopScore =", subjectTopScore)  # 每科最高分
print("topScore =", topScore)               # 全部最高分
print("studentSumScore =", studentSumScore)  # 每個同學總分
print("topScoreStudent =", topScoreStudent)  # 最高總分的同學
