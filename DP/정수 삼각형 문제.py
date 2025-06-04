# 풀이 횟수: 2
# 입력부
# 삼각형 높이 입력
N = int(input())
# 삼각형 배열 입력
triangle = []
for _ in range(N):
    triangle.append(list(map(int,input().split())))
result = 0
# 다음과 같은 삼각형 형태의 숫자 배열이 주어졌을 때, 
# 위에서부터 아래로 내려가면서 숫자를 더해 최대 합을 구하는 문제
# DFS로 풀기에는 중복 연산으로 인해 너무 많은 연산이 발생한다. 
#    1
#   2 3
#  4 5 6
# 7 8 9 10

# 하위 문제 정의
# 최대 합은 현재 배열의 값과, 아래에 위치한 두 값 중 최대 값을 더한 값이다.

# 점화식
# dp[j] = triangle[i][j] + max(dp[j] + dp[j+1])

# 초기화
# dp의 초기값은 triangle의 최하단 배열로 초기화한다.

# 상향식 접근
# 최하단 배열에서부터 위로 올라가면서 연산하고, 맨 위의 최종값을 구한다.

dp = triangle[-1]

for i in range(len(triangle)-2, -1, -1):
    for j in range(len(triangle[i])):
        dp[j] = triangle[i][j] + max(dp[j], dp[j+1])
    print(dp)

print(dp[0])




