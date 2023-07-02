#BOJ 15649 N과 M (1)
#순열 풀이
import sys
from itertools import permutations
N,M = map(int,sys.stdin.readline().split())
a = list(range(1,N+1))
answer = list(map(list,permutations(a,M)))
for i in answer:
    print(*i)
