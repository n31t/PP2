import re
txt = '''
a
aaa
llllaob
red_madrobot
abb_cvv
Aaafds

'''
x = re.findall('[A-Z]+[a-z]+', txt)
print(x)
