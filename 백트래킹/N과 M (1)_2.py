#BOJ 15649 N과 M (1)
#백트래킹 풀이
import sys
N,M = map(int,sys.stdin.readline().split())
s = []

def backTracking():
    if len(s) == M:
        print(*s)
    for i in range(1,N+1):
        if i not in s:
            s.append(i)
            backTracking()
            s.pop()

backTracking()
