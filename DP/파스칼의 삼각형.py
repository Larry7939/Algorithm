n, k = map(int,input().split())

dp = []
dp.append([1])
for i in range(0, n-1):
    dp.append([1]+[0]*i+[1])

for depth in range(2,n):
    for j in range(1, len(dp[depth])-1):
        dp[depth][j] += dp[depth-1][j-1] + dp[depth-1][j]
print(dp[n-1][k-1])