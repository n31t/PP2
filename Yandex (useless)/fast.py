n = int(input())
dohod = list(map(int, input().split()))
educ = list(map(int, input().split()))
free = list(map(int, input().split()))

# create a dictionary to store indices of countries that satisfy the conditions
country_dict = {}
for i in range(n):
    if free[i] == 1:
        country_dict[(0, 0, i+1)] = i+1
    else:
        country_dict[(dohod[i], educ[i], i+1)] = i+1

q = int(input())
dohod2 = list(map(int, input().split()))
educ2 = list(map(int, input().split()))
free2 = list(map(int, input().split()))

# look up the indices from the dictionary
country = [country_dict.get((dohod2[i], educ2[i], free2[i]), 0)
           for i in range(q)]
print(' '.join(map(str, country)))
