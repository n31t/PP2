def rvrs(s):
    listt = []
    num = ""
    for i in range(len(s)):
        if (s[i] == " "):
            listt.insert(0, num)
            num = ""
        else:
            num = num + s[i]

    if (i+1 == len(s)):
        listt.insert(0, num)
    for i in listt:
        print(i, end=' ')
    # return listt


s = str(input())
rvrs(s)
