n = input()

sus = n.find('h')
sas = n.rfind('h')
print(n[:sus]+n[sas:sus:-1]+n[sas+1:])
