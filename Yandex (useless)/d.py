n = int(input())
dohod = list(map(int, input().split()))
educ = list(map(int, input().split()))
free = list(map(int, input().split()))
q = int(input())
dohod2 = list(map(int, input().split()))
educ2 = list(map(int, input().split()))
free2 = list(map(int, input().split()))
country = []
for i in range(0, q):
    for j in range(0, n):
        if (free[j] == 1 and j+1 == free2[i] or (educ2[i] >= educ[j] and dohod2[i] >= dohod[j])):
            country.append(str(j+1))
            break
        else:
            if (j == n-1):
                country.append(str(0))
print(' '.join(country))
"""
2
10 9
1 0
0 1
5
0 0 11 10 9
0 1 0 1 1
2 1 0 0 0

"""
