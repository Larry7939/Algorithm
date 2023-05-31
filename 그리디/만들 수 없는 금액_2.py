import sys

n = int(sys.stdin.readline())
coins = list(map(int,sys.stdin.readline().strip().split()))

# 동전 오름차순 정렬
coins.sort()

# 목표값 설정
target = 1

# 동전 탐색
for coin in coins:
    # 현재 동전이 목표값보다 크다면, 해당 목표값은 만들 수 없음
    if target < coin:
        break
    #목표값 갱신
    target += coin

print(target)
# 핵심은 target 이하의 값은 모두 만들 수 있다는 개념을 정의하는 것이다. 