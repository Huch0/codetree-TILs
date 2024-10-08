N, M = map(int, input().split())

# combs = []

# def recur(comb, last):
#     if len(comb) == M:
#         combs.append(comb)
#         return
    
#     for i in range(last + 1, N + 1):
#         recur(comb + [i], i)

# recur([], 0)

# for comb in combs:
#     print(' '.join(map(str, comb)))

from itertools import combinations

combs = combinations(range(1, N + 1), M)

for comb in combs:
    print(' '.join(map(str, comb)))