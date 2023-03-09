a = list(map(int, input().split()))
x = '*'.join(str(i) for i in a)
print(eval(x))
