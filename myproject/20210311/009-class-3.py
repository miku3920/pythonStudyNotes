class MyClass:
    def __init__(self):
        print("init")

    def fun1(self):
        print("fun1")

    def fun2(self, a, b):
        print(a, b)

    def fun3(self, a=1, b=2):
        print(a, b)

    def fun4(self, a, b):
        return a+b

    def super(self):
        self.fun1()
        self.fun2(1, 2)
        self.fun3(a=3, b=4)
        x = self.fun4(5, 6)
        print(x)

a = MyClass()
a.fun3()
x = a.fun4(1, 2)
print(x)