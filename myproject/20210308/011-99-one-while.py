i = 1
j = 1

while True:
    print("%d * %d = %2d" % (i, j, i * j), end="\t")

    j += 1
    if j >= 10:
        print()
        i += 1
        j = 1

    if i >= 10:
        break