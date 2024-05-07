from itertools import combinations
N,M = map(int,input().split())
weights = list(map(int,input().split()))
a = [x for x in list(combinations(weights, 2)) if x[0] != x[1]]
# a = list(filter(lambda x: x[0] != x[1], list(combinations(weights, 2))))
print(len(a))