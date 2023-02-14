def pal_or_not(t):
    if t == t[::-1]:
        return True
    else:
        return False


t = input()
print(pal_or_not(t))
