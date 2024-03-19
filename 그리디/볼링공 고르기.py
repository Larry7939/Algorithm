# 풀이 횟수 2
import sys
n, m = map(int, sys.stdin.readline().split())
result = 0
weights = list(map(int, sys.stdin.readline().split()))
weight_count = [0]*(m+1)

# 각 무게의 개수를 카운트한다.
for i in range(1, m+1):
    weight_count[i] = weights.count(i)


for i in range(1, m+1):
    n -= weight_count[i]  # 무게가 i인 볼링공의 개수, 즉, A가 이미 선택한 볼링공의 무게의 개수를 제외한다.
    result += weight_count[i]*n # A가 선택한 볼링공 무게 이외의 나머지 볼링공들의 개수와 곱한 다음 result에 더해준다.
print(result)

# A가 특정 무게를 선택했을 때, B가 선택하는 경우를 차례대로 계산하면 된다.
# 각 무게의 개수를 카운트하여 일일이 경우의 수를 구하지 않고 곱셈으로 한꺼번에 경우의 수를 구하는 것이 핵심
# 혹은 combinations를 활용한 간단한 풀이법