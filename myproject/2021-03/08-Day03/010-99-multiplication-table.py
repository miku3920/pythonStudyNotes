i = 1
j = 1

while i < 10:
    while j < 10:
        print("%d * %d = %2d" % (i, j, i*j), end="\t")
        j += 1
    print()
    i += 1
    j = 1
