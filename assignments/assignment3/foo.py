
class Vehicle():
    def __init__(self, x):
        self.x = x

    def compare(self, them):
        print("here1", self.x, them.x, self.x==them.x)
        return self.x == them.x

    def printme(self):
        print("x=", self.x)

class Lorry(Vehicle):
    def __init__(self, x, weight):
        Vehicle.__init__(self, x)
        self.weight = weight

    def compare(self, them):
        print("here2", self.x, them.x, self.x==them.x)
        return self.x == them.x and self.weight == them.weight

    def printme(self):
        print("x=", self.x, "weight=", self.weight)


a = Vehicle("vehicle")
b = Lorry("lorry", 15)

a.printme()
b.printme()
a.compare(b)
b.compare(a)

