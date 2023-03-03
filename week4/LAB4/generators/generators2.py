n = int(input('N = '))


def mygenerator(n):
    for i in range(0, n):
        if (i % 2 == 1):
            yield i


listt = []
for val in mygenerator(n):
    listt.append(str(val))


print(', '.join(listt))
