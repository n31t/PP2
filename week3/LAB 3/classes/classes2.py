class Shape:
    def __init__(self):
        self.area = 0

    def areaa(self):
        print(self.area)


class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = int(length) * int(length)

    '''def area(self):
        print(self.area)'''


num = Square(int(input()))
num.areaa()
