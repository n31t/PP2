import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print('x =', self.x, 'y =', self.y)

    def move(self):
        x1 = int(input())
        self.x = self.x + x1
        y1 = int(input())
        self.y = self.y + y1

    def dist(self):
        x1 = int(input())
        y1 = int(input())
        lenx = abs(x1 - self.x)
        leny = abs(y1 - self.y)
        print('The distance is (', lenx, ',', leny, ') =',
              math.sqrt(lenx**2+leny**2))


num = Point(int(input()), int(input()))
num.show()
num.move()
num.show()
num.dist()
