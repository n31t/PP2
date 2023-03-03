def gen_print():
    listt = []
    for val in squares(n):
        listt.append(str(val))
    print(', '.join(listt))


n = int(input('a = '))
b = int(input('b = '))


def squares(n):
    for i in range(n, b):
        yield i*i


gen_print()
