from collections import deque
N,M = 5,5

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))
y,x = map(int,input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 1: 사과
# -1: 장애물

# 지나간 칸은 장애물로 변경된다. 즉, 왔던 길을 다시 갈 수 없다.
# 백트래킹을 활용하여, 사과를 3개 먹는 모든 경우의 수를 고려해야한다.

# 진행 과정
#  1. 도착한 곳을 -1로 바꾼다. graph[y][x] = -1
#  2. 현재 위치 정보를 저장한다
# 복원 과정
#  1. 방문한 곳을 다시 0으로 바꿔준다.
#  2. 진행 과정 2에서 저장한 위치 정보를 복원한다,
move_count = 0
apple_count = 0
result = []
def dfs(x,y, move_count, apple_count):
    if graph[y][x] == 1: 
        apple_count += 1

    before = graph[y][x]
    if apple_count == 3:
        result.append(move_count)
        return
    graph[y][x] = -1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0<= ny < 5 and graph[ny][nx] != -1:
            dfs(nx, ny, move_count + 1, apple_count)
    graph[y][x] = before

dfs(x,y, move_count, apple_count)

if len(result) == 0:
    print(-1)
else:
    print(min(result))