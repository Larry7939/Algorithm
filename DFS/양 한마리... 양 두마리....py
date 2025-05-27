import sys
sys.setrecursionlimit(10**7)
T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = []


def dfs(x,y):
    graph[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] != 1:
            dfs(nx,ny)
for _ in range(T):
    H, W = map(int,input().split())
    count = 0
    graph = [[] for _ in range(H)]
    for i in range(H):
        groups = list(''.join(input().split()))
        for group in groups:
            if group == '#':
                graph[i].append(0) # 양
            else:
                graph[i].append(1) # 풀
    for y in range(H):
        for x in range(W):
            if graph[y][x] == 0:
                count += 1
                dfs(x,y)
    result.append(count)
for r in result:
    print(r)