import re
txt = '''
a
aaa
llllaob
red_madrobot
abb_cvv
'''
# task 3
x = re.findall('[a-z]+_[a-z]+', txt)
print(x)
