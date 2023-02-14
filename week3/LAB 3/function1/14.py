from itertools import permutations


def next_permutation(s):
    perm = permutations(s)
    for i in perm:
        print(i)


def gr_to_ounc(grams):
    ounces = 28.3495231 * grams
    return ounces


def Cels(f):
    C = (5/9) * (f - 32)
    return C


def solve(numheads, numlegs):
    chic = 0
    rab = 0
    if (numlegs > numheads and numlegs % 2 == 0):
        rab = (numlegs - 2*numheads)/2
        chic = numheads - rab
    else:
        return ("No solution")
    return (int(chic), int(rab))


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

"""
numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))"""

"""print(Cels(0))"""

"""grams = int(input())
print(gr_to_ounc(grams))"""
