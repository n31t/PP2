n = str(input())
print(n[2])
print(n[-2])
print(n[:5])
print(n[:-2])
for i in range(len(n)):
    if i % 2 == 0:
        print(n[i], end="")

print()
for i in range(len(n)):
    if i % 2 == 1:
        print(n[i], end="")

print()
print(n[::-1])
print(n[::-2])
print(len(n))
