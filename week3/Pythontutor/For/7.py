sum = 0
f = 1
n = int(input())
for i in range(1,n+1):
    f = f * i
    sum = sum + f

print(sum)