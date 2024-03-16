# 풀이 횟수 2
import sys
from itertools import combinations
n = int(sys.stdin.readline().strip())
coins = list(map(int,sys.stdin.readline().strip().split()))
coinSum = []

# combinaitons로 순서를 고려하지 않고 중복없이 range(1,n+1)개씩 뽑아서 만들 수 있는 모든 합을 구한다.
# 구한 모든 합을 합 리스트에 append한다.
# 합 리스트를 오름차순 정렬하고, coinSum[-1]까지 1씩 증가시키는 반복문을 만든다.
# 증가시키는 인자가 coinSum[]에 존재하지 않으면 반복문을 끝내고 그 인자를 출력한다.
for i in range(1,n+1):
    for j in list(combinations(coins,i)):
        coinSum.append(sum(j))
coinSum.sort()
print(coinSum)
for i in range(1,coinSum[-1]+2):
    if i not in coinSum:
        print(i)
        break