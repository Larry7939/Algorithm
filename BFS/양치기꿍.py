from collections import deque
# 이중for문을 돌면서 .인 경우에만 bfs 호출
# nx,ny조건을 나눌 때, graph[ny][nx]가 #이 아닐 때에만 bfs(nx,ny)를 호출할 수 있도록 함.
# 한 번 호출될 때마다 while문이 끝날 때 변수 k와 v를 비교해서 작은 것은 0으로 만들기

R, C = map(int, input().split())
graph = []
for _ in range(R):
    a = list(input())
    graph.append(a)
visited = [[False]*C for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sheep = 0
wolf = 0


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited[y][x] = True
    global sheep, wolf
    s = 0
    w = 0
    while dq:
        x, y = dq.popleft()
        if graph[y][x] == 'v':
            w += 1
        elif graph[y][x] == 'k':
            s += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < C and 0 <= ny < R and visited[ny][nx] == False and graph[ny][nx] != '#':
                visited[ny][nx] = True #방문처리를 popleft시에 해주는 경우, visited의 효과가 사라져 특정 좌표를 동시에 두 번 append해주는 문제가 발생할 수 있다. 이렇게 하면 , 특정 좌표를 두 번 방문하는 문제가 발생한다.
                #특히 테케 1번의 (1,3) (2,2)에서 'k'가 위치한 (2,3)을 두번 append하는 불상사가 발생한다.
                dq.append((nx, ny)) 
    if not (w==0 and s==0):
        if w < s:
            sheep += s  # 양이 늑대보다 많은 경우
        else:
            wolf += w


for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visited[i][j]==False:
            bfs(j,i)
print(sheep,wolf)

        