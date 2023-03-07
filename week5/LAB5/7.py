import re


def f(mObject):
    return mObject.group("g1")+mObject.group("g2").upper()


txt = input()
pattern = "(?P<g1>[a-z])_{1}(?P<g2>[a-z]){1}"
print(re.sub(pattern, f, txt))
