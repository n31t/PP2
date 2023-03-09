import time
n = int(input('Sample Input:\n'))
milsec = int(input())
sec = milsec/1000
time.sleep(sec)
sqrt = n ** 0.5
txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(
    fnum=n, fsec=milsec, fsqrt=sqrt)
print(txt)
