import re
txt = '''
a
aaa
llllaob
red_mad_robot
'''
# task 1
#x = re.findall('.*a+.*', txt)
# print(x)

# task 2
x = re.findall(r".*a+.*b+.*b+.*b*.*", txt)

# task 3
x = re.search(r"([a-z]+_)+[a-z]+", file.read())
