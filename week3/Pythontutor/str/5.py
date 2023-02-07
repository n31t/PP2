n = str(input())
revers = n[::-1]
a = n.count('f')
if a > 0:
    if a == 1:
        print(n.find('f'))
    else:
        print(n.find('f'), len(n) - 1 - revers.find('f'))
