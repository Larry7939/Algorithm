# 가로, 세로, 대각선 이동 가능
# 1은 땅, 0은 바다
# 너비 w, 높이 h 입력
# 1과 0으로 구성된 지도 입력
# 테스트 케이스 여러 개에 대해서 동작하고, 00이 입력될 때까지 테스트 케이스 입력
# 섬의 개수 출력
# 지도상 값이 1인 모든 좌표에 대해서 카운트 + 1 후에 dfs 호출
# 연결된 모든 섬을 0으로 만든다. 
# dfs호출 후 count를 출력하고 0으로 만든다.(다음 케이스를 위한 초기화)
import sys
sys.setrecursionlimit(10**7)
dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]
dd = [(-1,-1),(1,-1),(-1,1),(1,1)] # 좌상, 우상, 좌하, 우하

def dfs(graph, x, y):
    graph[y][x] = 0
    for i in range(4):
        if 0 <= x+dx[i] < w and 0 <= y+dy[i] < h:
            if graph[y+dy[i]][x+dx[i]] == 1:
                dfs(graph, x+dx[i], y+dy[i])
        if 0 <= x+dd[i][0] < w and 0 <= y+dd[i][1] < h:
            if graph[y+dd[i][1]][x+dd[i][0]] == 1:
                dfs(graph, x+dd[i][0], y+dd[i][1])

while True:
    result = 0
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                result += 1
                dfs(graph, x, y)
    print(result)
    result = 0

        