class Myclass:
    x = 5
    y = 10
print(Myclass)
p1 = Myclass()
print(p1.x)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
    def __init__(self,name,age):
        pass
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

#del p1.age

#print(p1.age) - error
#del p1

class Person:
  pass

class MyClass:
  x = 5

class MyClass:
  x = 5

p1 = Myclass()
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age