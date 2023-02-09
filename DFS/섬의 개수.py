import sys
sys.setrecursionlimit(10000)
# 매번 입력을 마칠 때마다 answer에 섬의 개수를 append하면 될듯?
answer = []
# 상하좌우 대각선에 대해서 모두 dfs호출하는데, 이 때 인덱스 검사를 한다.
# 이미 graph[y][x]가 1인 시점에서 True 반환은 확정되어있고, 붙어있는 섬을 하나로 인식하기 위해, 붙어있는 섬들을 모두 0으로 만들어줘야함.

# 상하좌우 좌상, 우상, 좌하, 우하
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, 1, 1, -1, -1]

# dfs
def dfs(x, y):
    if graph[y][x] == 1:
        graph[y][x] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (-1 < nx < w) and (-1 < ny < h):
                dfs(nx, ny)
        return True
    return False

while True:
    result = 0
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [[] for _ in range(h)]
    for i in range(h):
        a = list(map(int, input().split()))
        graph[i] = a
    for x in range(h):
        for y in range(w):
            if dfs(y, x):
                result += 1
    answer.append(result)
for i in answer:
    print(i)