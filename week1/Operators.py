print(10 + 5)
x = 5
y = 3

print(x - y)
x = 5
y = 3

print(x * y)
x = 12
y = 3

print(x / y)
x = 5
y = 2

print(x % y)

x = 2
y = 5

print(x ** y)  # same as 2*2*2*2*2
x = 15
y = 2

print(x // y)

# the floor division // rounds the result down to the nearest whole number
x = 5

print(x)
x = 5

x += 3

print(x)
x = 5

x -= 3

print(x)
x = 5

x *= 3

print(x)
x = 5

x /= 3

print(x)
x = 5

x %= 3

print(x)
x = 5

x %= 3

print(x)
x = 5

x **= 3

print(x)
x = 5

x |= 3

print(x)
x = 5

x ^= 3

print(x)
x = 5

x >>= 3

print(x)
x = 5

x <<= 3

print(x)


x = 5
y = 3

print(x == y)
x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3

x = 5
y = 3

print(x > y)

# returns True because 5 is greater than 3
x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3
x = 5
y = 3

print(x >= y)

# returns True because five is greater, or equal, to 3
x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
x = 5

print(not (x > 3 and x < 10))

# returns False because not is used to reverse the result

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
"""E x E R C I s E S"""
print(10*5)
print(10/2)
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

if 5 != 10:
    print("5 and 10 is not equal")


# returns False because 5 is not equal to 3
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")
