from itertools import permutations


def next_permutation(s):
    perm = permutations(s)
    for i in perm:
        print(i)


next_permutation(str(input()))
