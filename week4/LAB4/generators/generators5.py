def gen_print():
    listt = []
    for val in mygen(n):
        listt.append(str(val))
    print(', '.join(listt))


n = int(input('N = '))


def mygen(n):
    for i in range(n, -1, -1):
        yield i


gen_print()
