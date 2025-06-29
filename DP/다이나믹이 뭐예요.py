m,n = map(int,input().split())

dp = [[0]*m for _ in range(n)]
# dfs로 가면서 각 지점에 방문할 때마다 dp[y][x]에 + 1 씩 해준다. -> 이렇게 하면 안된다
# 각 지점을 방문하면서 이전 지점의 dp를 더해준다. 이를 위해서 x,y를 넘겨주거나 dp값을 넘겨줘야할듯?

# 아니면 dfs 없이 오른쪽, 아래, 우하향 대각선으로만 이동 가능하니까, 역으로 x-1,y, x-1,y-1, x,y-1에 있는 걸 더하는 건?
dp[0][0] = 1
for x in range(m):
    for y in range(n):
        if 0 <= y-1: 
            dp[y][x] += dp[y-1][x]
        if 0 <= y-1 and 0 <= x-1:
            dp[y][x] += dp[y-1][x-1]
        if 0 <= x-1:
            dp[y][x] += dp[y][x-1]
print(dp[n-1][m-1] % 1000000007)        
