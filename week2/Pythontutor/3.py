a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((a + b) % 2 == 0 and (c + d) % 2 == 0) or ((a + b) % 2 != 0 and (c + d) % 2 != 0):
    print('YES')
else:
    print('NO')
