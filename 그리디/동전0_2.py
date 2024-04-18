from collections import deque
# 동전 개수 N, 목표 금액 K
# 동전의 가치 리스트 values

# 가장 큰 동전부터 K에서 나누기 및 나머지 연산,
N, K = map(int, input().split())
values = deque()
for _ in range(N):
    values.appendleft(int(input()))
coin_count = 0
for v in values:
    if K >= v:
        coin_count += K // v
        K = K % v
print(coin_count)