def fun1():
    print("fun1")

def fun2(a, b):
    print(a, b)

def fun3(a=1, b=2):
    print(a, b)

def fun4(a, b):
    return a+b

def super():
    fun1()
    fun2(1, 2)
    fun3(a=3, b=4)
    x = fun4(5, 6)
    print(x)
