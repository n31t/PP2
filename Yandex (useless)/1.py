n, x, t = list(map(int, input().split()))
a = list(map(int, input().split()))
a2 = []
for i in a:
    a2.append(abs(i - x))
a3 = a2.copy()
a3.sort()
# print(a2)
sum = t
k = 0
for i in a3:
    if (i <= sum):
        sum = sum - i
        k = k + 1
        for j in range(len(a2)):
            if (i == a2[j]):
                a2[j] = -1
                break
    else:
        break
print(k)
listt = []
for l in range(len(a2)):
    if (a2[l] == -1):
        listt.append(str(l+1))
        #print(l+1, ' ', end='')
print(' '.join(listt))
'''
5 19 32
36 10 72 4 50 /2
4 25 10
1 10 42 9
/0
'''
