nxt = list(map(int, input().split()))
s = list(map(int, input().split()))
differences = [abs(s[i] - nxt[1]) for i in range(nxt[0])]
s = sorted(range(len(differences)), key=lambda k: differences[k])
z, n, k, l = 0, 0, 0, []
while n < len(differences) and z + differences[s[n]] <= nxt[2]:
    k += 1
    l.append(s[n] + 1)
    z += differences[s[n]]
    n += 1
print(k)
print(" ".join(map(str, l)))
