for i in range(10):
    for j in range(10):
        if i != 4 and j != 4:
            print("%d * %d = %2d" % (i, j, i*j), end="\t")
    print()
