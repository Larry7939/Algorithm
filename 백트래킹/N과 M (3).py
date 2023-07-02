#BOJ 15651 N과 M(3)
import sys
N,M = map(int,sys.stdin.readline().split())

s = []
def backTracking():
    if len(s) == M:
        print(*s)
        return
    for i in range(1,N+1):
        s.append(i)
        backTracking()
        s.pop()

backTracking()