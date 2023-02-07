n = int(input())
sum1 = 0
sum2 = 0
for i in range(1,n+1):
    sum1 += i

for i in range(1,n):
    a = int(input())
    sum2 += a
#print(sum1,sum2)
print(sum1 - sum2)