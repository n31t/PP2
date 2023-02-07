str = str(input())
l = len(str)//2
a = str[:len(str)-l]
b = str[len(str)-l:]
print(b+a)
