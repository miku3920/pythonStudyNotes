from opencc import OpenCC
text1 = "我去过清华大学和交通大学，打印机、光盘、内存。"
text2 = "我去過清華大學和交通大學，印表機、光碟、記憶體。"

print("      "+text1) # 我去过清华大学和交通大学，打印机、光盘、内存。

openCC = OpenCC('s2t')
line = openCC.convert(text1)
print("s2t  :"+line) # 我去過清華大學和交通大學，打印機、光盤、內存。

openCC.set_conversion('s2twp')
line = openCC.convert(text1)
print("s2twp:"+line) # 我去過清華大學和交通大學，印表機、光碟、記憶體。


print("      "+text2) # 我去過清華大學和交通大學，印表機、光碟、記憶體。

openCC.set_conversion('t2s')
line = openCC.convert(text2)
print("t2s  :"+line) # 去过清华大学和交通大学，印表机、光碟、记忆体。

openCC.set_conversion('tw2sp')
line = openCC.convert(text2)
print("tw2sp:"+line) # 我去过清华大学和交通大学，打印机、光盘、内存。
