# 풀이 횟수 2
#BOJ 16435 스네이크버드
import sys
#과일 높이 정렬
#스네이크버드의 길이보다 작거나 같은 경우, 길이 + 1

n,l = map(int,sys.stdin.readline().split())
h = list(map(int,sys.stdin.readline().split()))
h.sort()
for i in h:
    if l >= i:
        l+=1
    else:
        break

print(l)