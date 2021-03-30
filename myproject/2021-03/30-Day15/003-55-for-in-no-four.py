x = int(input("輸入乘法表最大值: "))

for i in range(1,x+1):
    for j in range(1,x+1):
        if i != 4 and j != 4:
            print("%2d * %2d = %3d" % (j, i, j * i), end="\t")
    print()