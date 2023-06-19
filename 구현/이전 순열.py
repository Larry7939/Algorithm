#BOJ 10973 이전순열
from itertools import permutations
import sys

n = int(sys.stdin.readline())
match_list = tuple(map(int,sys.stdin.readline().split()))
x = list(permutations(list(range(1,n+1)),n))
x.sort()

match_index = x.index(match_list)
if match_index == 0:
    print(-1)
else:
    print(*x[match_index-1])