str = str(input())
up = 0
low = 0
for i in str:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
print(f"Upper case letters are {up}", f'Lower case letters are {low}')
