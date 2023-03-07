n = int(input())
dohod = list(map(int, input().split()))  # input n numbers only
educ = list(map(int, input().split()))  # input n numbers only
free = list(map(int, input().split()))  # input n numbers only
q = int(input())
dohod2 = list(map(int, input().split()))  # input q numbers only
educ2 = list(map(int, input().split()))  # input q numbers only
free2 = list(map(int, input().split()))  # input q numbers only
country = []
for i in range(0, q):
    for j in range(0, n):
        if (free[j] == 1 and j+1 == free2[i]):
            country.append(str(j+1))
            break
        elif (educ2[i] >= educ[j]):
            if (dohod2[i] >= dohod[j]):
                country.append(str(j+1))
                break
            else:
                if (j == n-1):
                    country.append(str(0))
        else:
            if (j == n-1):
                country.append(str(0))
print(' '.join(country))

'''
Input:
2
10 9
1 0
0 1
5
0 0 11 10 9
0 1 0 1 1
2 1 0 0 0
Output:
2 0 2 1 2 
'''
