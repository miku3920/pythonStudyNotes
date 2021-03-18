def setLocalValue():
    x = 1
    a = 1
    print("local x=", x, "local a=", a)


# def printLocalValue():  # error
    # print("local x=", x)


def printGlobalValue():
    print("global y=", y)


def setGlobalValue():
    global z
    z = 3


a = 0
setLocalValue()  # 設定一些區域變數
# print("local x=", x)  # error # 在外面印裡面的東西
# printLocalValue()  # error #在另一個裡面印裡面的東西
print("global a=", a)  # 在外面印外面的 a (沒被改掉)

y = 1
printGlobalValue()  # 在裡面印外面的 y

z = 2
setGlobalValue()  # 在裡面設定 z 成全域變數，並修改 z 的值
print("global z=", z)  # 印出被改過的 z
