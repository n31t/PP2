n, x, t = map(int, input().split())
a = list(map(int, input().split()))
a2 = [abs(i - x) for i in a]
remaining_time = t
k = 0
selected_indices = set()
for i in sorted(a2, key=lambda x: x):
    if i <= remaining_time:
        remaining_time -= i
        k += 1
        for j, val in enumerate(a2):
            if val == i and j not in selected_indices:
                selected_indices.add(j)
                break
    else:
        break
print(k)
print(" ".join(str(i+1) for i in sorted(selected_indices)))
