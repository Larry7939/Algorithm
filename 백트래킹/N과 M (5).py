#BOJ 15651 N과 M(4)
import sys
N,M = map(int,sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().split()))
s.sort()
answer = []
#s를 돌며 본인을 제외한 다른 원소들 append하기
def backTracking():
    if len(answer) == M:
        print(*answer)
        return
    for i in s:
        if i not in answer:
            answer.append(i)
            backTracking()
            answer.pop()
backTracking()