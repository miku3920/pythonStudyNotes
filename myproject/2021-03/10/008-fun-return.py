def return123():
    return 123, 456


def returnInt():
    return 25


def returnFloat():
    return 12.5


def returnStr():
    return "Hello"


def returnList():
    return [1, 2, 3]


x, y = return123()
print(x, y)
x = returnInt()
print(x)
x = returnFloat()
print(x)
x = returnStr()
print(x)
x = returnList()
print(x)
