a = int(input())
b = int(input())
arr = []
if a>b:
    for i in range(b,a+1):
        arr.append(i)
else:
    for a in range(a,b+1):
        arr.append(a)

if a>b:
    arr.reverse()
for x in arr:
    print(x)