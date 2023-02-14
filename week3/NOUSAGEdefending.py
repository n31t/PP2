class Cars:
    def __init__(self, engine, mark, color):
        self.engine = engine
        self.mark = mark
        self.color = color

    def printinfo(self):
        print("Engine =", self.engine, "Mark =",
              self.mark, "Color =", self.color)


class Toyota(Cars):
    def __init__(self, engine, mark, color, country):
        #self.engine = engine
        #self.mark = mark
        #self.color = color
        Cars.__init__(self, engine, mark, color)
        self.country = country
        self.price = 'undefined, please add price with f(setter)'

    def printinfo(self):
        print("Engine =", self.engine, "Mark =", self.mark,
              "Color =", self.color, "Country =", self.country)

    def setter(self):
        self.price = int(input())

    def getter(self):
        print(self.price, "tenge")


class Camry(Toyota):
    def __init__(self, engine, mark, color, country):
        Toyota.__init__(self, engine, mark, color, country)
        self.wheels = 4

    def printinfo(self):
        Toyota.printinfo(self)
        print("Wheels =", self.wheels)
        '''print("Engine =", self.engine, "Mark =", self.mark,
              "Color =", self.color, "Country =", self.country, "Wheels =", self.wheels)'''


v = Camry(str(input()), str(input()), str(input()), str(input()))
v.printinfo()

"""v = Toyota(str(input()), str(input()), str(input()), str(input()))
v.printinfo()
v.setter()
v.getter()"""
