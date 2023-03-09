str = str(input())
x = 0
for a, b in zip(str, str[::-1]):
    if a != b:
        print('It\'s not a palindrome')
        x = 1
        break
if (x == 0):
    print('Is\'s a palindrome')
# Or just like that
# str = input()
# if txt == txt[::-1]:
#     print("Is\'s a palindrome")
# else:
#     print("It\'s not a palindrome'")
