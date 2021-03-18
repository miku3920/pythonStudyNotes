class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)

    def printAge(self):
        print(self.age)


alex = People("alex", 18)
alex.printName()
alex.printAge()

bob = People("bob", 20)
bob.printName()
bob.printAge()
