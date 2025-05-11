# 풀이 횟수 3
#BOJ 3135 라디오
import sys
a,b = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
result = abs(a-b)
#다른 버튼을 입력할 때마다, 기존에 존재하는 방법과 비교

for _ in range(n):
    k = int(sys.stdin.readline())
    if result > abs(k-b):
        result = abs(k-b) + 1 #a-b를 그대로 쓰는 것이 아닌 경우에는 버튼을 누르는 것이므로 + 1
print(result)