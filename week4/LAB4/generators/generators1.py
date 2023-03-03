
#n = int(input('N = '))


''' Solution (ITERATOR)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < n:
            x = pow(self.a, 2)
            self.a = self.a+1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)'''

n = int(input('N = '))


def mygenerator(n):
    for i in range(1, n):
        yield i*i


for val in mygenerator(n):
    print(val)
