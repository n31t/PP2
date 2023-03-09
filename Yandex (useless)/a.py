num = int(input())
k = list(map(int, input().split()))
r = list(map(int, input().split()))
w = dict(zip(k, r))
num2 = int(input())
text = list(map(int, input().split()))
counter = 0
'''counter = sum(1 for a, b in zip(
    text, text[1:]) if w[a] != w[b])'''
for a, b in zip(text, text[1:]):
    if w[a] != w[b]:
        counter += 1
print(counter)
'''
4
1 2 3 4
1 2 1 2
5
1 2 3 1 4

'''
