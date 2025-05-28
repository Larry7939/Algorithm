import sys
sys.setrecursionlimit(10**7)

M,N,K = map(int,input().split())
# M: 높이, N: 너비, K: 영역 좌표 입력 횟수
# 그래프 초기화
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    extent = 1
    graph[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and graph[ny][nx] != 1:
            extent += dfs(nx,ny)
    return extent
count = 0 #영역 개수
extent = [] #넓이
for i in range(0,M):
    for j in range(0, N):
        if graph[i][j] == 0:
            count += 1
            extent.append(dfs(j,i))
extent.sort()
print(count)
print(*extent)