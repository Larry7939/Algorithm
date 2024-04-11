# graph 순회하다가 0을 발견하면 카운트하고 dfs를 수행하여 연결된 모든 칸을 1로 만든다.
def dfs(graph, x, y):
    graph[y][x] = 1
    for i in range(4):
        if 0 <= x+dx[i] < w and 0 <= y+dy[i] < h:
            if graph[y+dy[i]][x+dx[i]] == 0:
                dfs(graph, x+dx[i], y+dy[i])
                


h, w = map(int,input().split())
graph = []
result = 0
dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0] 
for _ in range(h):
    graph.append(list(map(int,input())))
for y in range(h):
    for x in range(w):
        if graph[y][x] == 0:
            result += 1
            dfs(graph, x, y)
            for i in range(h):
                print(*graph[i])
print(result)
    