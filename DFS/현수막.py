import sys
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int,input().split()))

dx = [0,0,-1,1,-1,-1,1,1] #상하좌우 좌상 좌하 우상 우하
dy = [-1,1,0,0,-1,1,-1,1]
cnt = 0
def dfs(x,y):
    graph[y][x] = 0
    for i in range(8):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 1:
            dfs(nx,ny)

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            dfs(j,i)
            cnt += 1
print(cnt)