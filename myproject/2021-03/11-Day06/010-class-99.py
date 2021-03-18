class MultiplicationTable:
    maxX = 0
    maxY = 0

    def __init__(self, maxX, maxY):
        self.maxX = maxX
        self.maxY = maxY

    def print(self):
        i = 1
        while i <= self.maxY:
            j = 1
            while j <= self.maxX:
                print("%2d * %2d = %3d" % (j, i, j * i), end="\t")
                j += 1
            print()
            i += 1


a = MultiplicationTable(3, 4)
a.print()
