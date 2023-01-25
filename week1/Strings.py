print("Hello")
print('Hello')
a = "Hello"
print(a)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

'''COMMENT'''

print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)
# b a n a n a
a = "Hello, World!"
print(len(a))  # SIZE == LEN!!!!

txt = "The best things in life are free!"
print("free" in txt)  # checks it (boolean)
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])  # 2 - 4

b = "Hello, World!"
print(b[:5])  # 1 - 4

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])  # -5 to -2

a = "Hello, World!"
print(a.upper())  # caps

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())
##########################################
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John and I am {}."
print(txt)
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# exrcises
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World! "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("Hello", "World")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
