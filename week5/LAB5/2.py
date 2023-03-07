import re
txt = '''
a
aaa
llllaob
ao0bbbb
red_mad_robot
'''
x = re.findall(r".*a+.*b+.*b+.*b?.*", txt)
print(x)
