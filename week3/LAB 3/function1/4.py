

def isPrime():
    listt = []
    num = ""
    s = str(input())
    for i in range(len(s)):
        if (s[i] == " "):
            listt.append(int(num))
            num = ""
        else:
            num = num + s[i]

    if (i+1 == len(s)):
        listt.append(int(num))

    return list(filter(lambda x: all(x % i != 0 for i in range(2, x)) and x >= 2, listt))


print(isPrime())


"""listt = []
num = ""


def isPrime(listt):
    return list(filter(lambda x: all(x % i != 0 for i in range(2, x)) and x >= 2, listt))


s = str(input())
for i in range(len(s)):
    if (s[i] == " "):
        listt.append(int(num))
        num = ""
    num = num + s[i]

    if (i+1 == len(s)):
        listt.append(int(num))

print(isPrime(listt))

"""
