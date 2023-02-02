x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1//2 < x2:
    if y1//2 < y2:
        if x1-x2 < y1-y2:
            print(x1-x2)
        else:
            print(y1-y2)
    else:
        if x1-x2 > y2:
            print(y2)
        else:
            print(x1-x2)
else:
    if y1//2 < y2:
        if x2 < y1-y2:
            print(x2)
        else:
            print(y1-y2)
    else:
        if y2 < x2:
            print(y2)
        else:
            print(x2)
