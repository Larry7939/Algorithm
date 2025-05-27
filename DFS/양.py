import sys
sys.setrecursionlimit(10**7)

R, C = map(int,input().split())

graph = []
dx = [0, 0, -1, 1]
dy = [-1,1, 0,0]
def dfs(x,y):
    sheep = 0
    wolf = 0
    if graph[y][x] == 'o':
        sheep += 1
    elif graph[y][x] == 'v':
        wolf += 1    
    graph[y][x] = '#'
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] != '#':
            s,w = dfs(nx,ny)
            sheep += s
            wolf += w
    return (sheep, wolf)

for r in range(R):
    graph.append(list(''.join(input().split())))


total_wolf = 0
total_sheep = 0
for x in range(C):
    for y in range(R):
        if graph[y][x] != '#':
            sheep, wolf = dfs(x, y)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
print(total_sheep, total_wolf)