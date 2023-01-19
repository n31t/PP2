x = 5
y = "John"
print(x)
print(y)
x = 4
x = "Sally"
print(x)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
# A will not overwrite a

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ['banana', "apple", "M879MOTOR", "strawberry"]
x, y, z, w = fruits  # must be equal
print(x)
print(y)
print(z)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x, y)

x = "awesome"


def myfunc():
    print("Is Python", x, '?')


myfunc()
