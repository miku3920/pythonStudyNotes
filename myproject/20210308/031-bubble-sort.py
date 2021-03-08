array = [15, 1, 4, 2, 8]
index = 0
l = len(array)

while True:
    finish = 1
    for i in range(0, l - 1):
        if array[i] > array[i + 1]:
            tmp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = tmp
            finish = 0
    if finish:
        break

print(array)
