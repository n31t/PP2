import re
txt = '''
alllldb
'''
x = re.findall(r".*a.*b$", txt)
print(x)
