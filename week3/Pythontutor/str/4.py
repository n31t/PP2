n = str(input())
a = int(n.find(" "))
print(n[a+1:]+" "+n[:a])
