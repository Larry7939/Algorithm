# BOJ 15650 N과 M (2)
import sys

N, M = map(int, sys.stdin.readline().split())

s = []


def backTracking(num):
    if len(s) == M:
        print(*s)
        return
    for i in range(num, N+1):
        if i not in s:
            s.append(i)
            backTracking(i+1)
            s.pop()
backTracking(1)