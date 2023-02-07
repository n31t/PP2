n = str(input())
sus = n[::-1]
a = sus.find('h')+1
print(n[:n.find('h')]+n[-a+1:])
