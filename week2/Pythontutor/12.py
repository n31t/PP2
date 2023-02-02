x = int(input())
y = int(input())
z = int(input())
if x*y < z:
    print('NO')
elif (x*y-z) % x == 0 or (x*y-z) % y == 0:
    print("YES")
else:
    print("NO")
