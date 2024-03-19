# 풀이 횟수 2
#BOJ 11047 동전 0

# N개 종류 동전으로 K 값을 만들기 위해 필요한 동전의 최소 개수
# 거스름돈 문제와 동일하게, 가장 큰 동전으로 먼저 연산하고, 나머지 연산을 해서 반영하면 된다.

N,K = map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
answer = 0
for coin in coins:
    if coin <= K:
        answer += K // coin
        K %= coin
print(answer)