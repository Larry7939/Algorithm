# BOJ 1189
import sys
input = sys.stdin.readline

# 상하좌우로 이동 - 반복문 안에서 dfs호출
# global answer
# 반복문에 들어가기 전에 거리가 K인지를 체크하고, answer+=1을 해줌.
# 반복문 안에서 상하좌우 이동 - nx,ny를 만들고 인덱스 체크
# T인지 .인지 구분 체크
# dfs(nx,ny로 이동)
# dfs에서 나온 후 에는 visited를 원상복구해주면서 나오자!
# =>이렇게 함으로써 매번 경로를 다녀올 때마다 그래프와 visited는 새 것이 되어있는 것임.

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, count):
    global answer
    visited[y][x] = 1
    if [x, y] == [C-1, 0]:
        if count == K:
            answer += 1
        return #목적지에 도달했다면 이하의 반복문은 수행할 필요가 없음. return함으로써 64ms만큼의 시간을 단축시킬 수 있다.
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < C and 0 <= ny < R and visited[ny][nx] == 0 and graph[ny][nx] !='T':
            visited[ny][nx] = 1
            dfs(nx,ny,count+1)
            visited[ny][nx] = 0


# 입력
# R(높이), C(너비), K(거리)
R, C, K = map(int, input().split())
answer = 0
graph = [['.' for _ in range(C)] for _ in range(R)]
for i in range(R):
    graph[i] = input()
visited = [[0 for _ in range(C)] for _ in range(R)]
dfs(0, R-1, 1)
print(answer)