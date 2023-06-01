import sys
#만들 수 없는 금액

# 1 1 2 3 9
# 다음 동전이 현재까지의 합보다 크면, 만들 수 없는 금액이다.
n = int(sys.stdin.readline())
coins = list(map(int,sys.stdin.readline().rstrip().split()))
coins.sort()
target = 1 
for coin in coins:
    if target < coin:
        break
    target += coin
print(target)
