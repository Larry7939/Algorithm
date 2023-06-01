import sys
# 숫자 카드 게임

n,m = map(int,sys.stdin.readline().split())
result = -1
for _ in range(n):
    row = list(map(int,sys.stdin.readline().split()))
    result = max(result,min(row))
print(result)
