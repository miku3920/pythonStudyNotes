import jieba
text1="我去過清華大學和交通大學。"
test2="小明來到了航研大廈"

seg_list = jieba.cut(text1, cut_all=True, HMM=False)
print("Full Mode: " + "/ ".join(seg_list))
# Full Mode: 我/ 去/ 過/ 清華/ 華大/ 大學/ 和/ 交通/ 交通大/ 大學/ /

seg_list = jieba.cut(text1, cut_all=False, HMM=True)
print("Default Mode: " + "/ ".join(seg_list))
# Default Mode: 我/ 去過/ 清華/ 大學/ 和/ 交通/ 大學/ 。
print(", ".join(jieba.cut(test2, HMM=True)))
# 小明, 來到, 了, 航研, 大廈
print(", ".join(jieba.cut(test2, HMM=False)))
# 小明, 來到, 了, 航, 研, 大廈
print(", ".join(jieba.cut(test2)))
# 小明, 來到, 了, 航研, 大廈
print(", ".join(jieba.cut_for_search(test2) ))
# 小明, 來到, 了, 航研, 大廈
