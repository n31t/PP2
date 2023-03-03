n = int(input('N = '))


def mygen(n):
    for i in range(n):
        if (i % 3 == 0 and i % 4 == 0):
            yield i


listt = []
for val in mygen(n):
    listt.append(str(val))


print(', '.join(listt))
