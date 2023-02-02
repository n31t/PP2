z = 1
arr = []
for i in range(3):
    x = int(input())
    arr.append(x)
if (arr[0] == arr[1]):
    z += 1
if (arr[0] == arr[2]):
    z += 1
if (arr[1] == arr[2]):
    z += 1
if z == 4:
    print(3)
else:
    print(z)
