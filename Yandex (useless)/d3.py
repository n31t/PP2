n = int(input())
dohod = list(map(int, input().split()))
educ = list(map(int, input().split()))
free = list(map(int, input().split()))
q = int(input())
dohod2 = list(map(int, input().split()))
educ2 = list(map(int, input().split()))
free2 = list(map(int, input().split()))


def get_country_idx(dohod_val, educ_val, free_idx):
    for i in range(n):
        if free[i] == 1 and i+1 == free_idx:
            return i+1
        elif educ[i] <= educ_val and dohod[i] <= dohod_val:
            return i+1
    return 0


country = [get_country_idx(dohod2[i], educ2[i], free2[i]) for i in range(q)]
print(' '.join(map(str, country)))
