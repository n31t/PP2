class Shape:
    def __init__(self):
        self.area = 0

    def areaa(self):
        print(self.area)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = int(width) * int(length)


num = Rectangle(int(input()), int(input()))
num.areaa()
