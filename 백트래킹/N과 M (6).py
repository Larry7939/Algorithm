#BOJ 15651 N과 M(4)
import sys
N,M = map(int,sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().split()))
s.sort()
answer = []
def backTracking(num):
    if len(answer) == M:
        print(*answer)
        return
    for i in range(num,len(s)):
        if s[i] not in answer:
            answer.append(s[i])
            backTracking(i+1)
            answer.pop()


backTracking(0)