x = int(input("輸入乘法表最大值: "))

i = 1
while i <= x:
    j = 1
    while j <= x:
        print("%2d * %2d = %3d" % (j, i, j * i), end="\t")
        j += 1
    print()
    i += 1