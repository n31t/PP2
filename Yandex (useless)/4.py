nxt = list(map(int, input().split()))
s = list(map(int, input().split()))
d = [abs(si - nxt[1]) for si in s]
sorted_indices = sorted(range(len(d)), key=lambda k: d[k])
num_items = 0
total_weight = 0
selected_indices = []
for i in sorted_indices:
    item_weight = d[i]
    if total_weight + item_weight > nxt[2]:
        break
    num_items += 1
    selected_indices.append(i + 1)
    total_weight += item_weight
print(num_items)
print(" ".join(map(str, selected_indices)))
'''
5 19 32
36 10 72 4 50 /2
4 25 10
1 10 42 9
/0
'''

