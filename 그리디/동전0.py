#BOJ 11047 동전 0
import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
coins = deque()
answer = 0
#동전을 내림차순으로 정렬한 후, 몫 및 나머지 연산
for _ in range(n):
    coins.appendleft(int(sys.stdin.readline()))

for coin in coins:
    if k >= coin:
        answer += k//coin
        k = k % coin
        
print(answer)
