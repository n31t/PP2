a = int(input())

min = a % 60
hrs = int((a - min)/60)
print(hrs % 24)
print(min)
