import re
txt = '''
nernnero imerimer,ofnrmer.wpomermpr
'''
x = re.sub('[ .,]', ':', txt)
print(x)
