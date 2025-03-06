# 입력부
# N(호반우의 개수)
# banus =[](각 호반우의 품질)
# result = 0
# 가장 좋은 품질의 호반우와 가장 나쁜 품질의 호반우를 묶는 것이 핵심
# 2, 4, 8, 9
# 위 경우, (2,9) = 18, (4,8) = 16, => 34
N = int(input())
banus = list(map(int, input().split()))
banus.sort()
result = 0
# 1. banus 오름차순 정렬
# 2. banus의 좌우 맨 끝의 값을 묶기
# 3. 값 계산하기
# 4. N이 홀수인 경우, result에 더하기
# 1, 2, 3, 4, 5 -> 10 + 8 + 3 -> 21
for i in range(N//2):
    result += banus[N-i-1] * 2

if N % 2 != 0:
    result += banus[N//2]
print(result)

# 어떻게 묶으면 가장 높은 가치를 받을 수 있는 지, 여러 케이스로 계산해보는 것이 핵심