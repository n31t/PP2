n = str(input())
revers = n[::-1]
a = n.count('f')
if a > 0:
    if a == 1:
        print(-1)
    else:
        sus = n[:n.find('f')]+n[n.find('f')+1:]
        print(sus.find('f')+1)
else:
    print(-2)
