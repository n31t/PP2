print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
''' RETURNS TRUE
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
    def __len__(self):
        return 0


m = myclass()
print(bool(m))


def myFunction():
    return True


print(myFunction())


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))
"""EXERCICES"""
# print(10 > 9) returns TRUE
print(10 == 9)
print(10 < 9)
print(bool("abc"))
print(bool(0))
