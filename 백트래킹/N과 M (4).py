#BOJ 15651 N과 M(4)
import sys
N,M = map(int,sys.stdin.readline().split())

s = []
def backTracking(num):
    if len(s) == M:
        print(*s)
        return
    for i in range(num,N+1):
        s.append(i)
        backTracking(i)
        s.pop()

backTracking(1)