def solve(numheads, numlegs):
    chic = 0
    rab = 0
    if (numlegs > numheads and numlegs % 2 == 0):
        rab = (numlegs - 2*numheads)/2
        chic = numheads - rab
    else:
        return ("No solution")
    return (int(chic), int(rab))


numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))
