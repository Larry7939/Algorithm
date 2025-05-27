R,C,K = map(int,input().split())
graph = [[] for _ in range(R)]
for i in range(R):
    locations = list(''.join(input().split()))
    for location in locations:
        if location == '.':
            graph[i].append(0)
        elif location == 'T':
            graph[i].append(-1)

startX = 0
startY = R-1

endX = C-1
endY = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 진행 과정
#  현재 좌표를 before에 저장
#  graph 상의 현재 좌표를 -1로 변경
# 복원 과정
#  graph 상의 현재 좌표를 before로 변경
result = []
# print(graph)
def dfs(x, y, move_count):
    if x == C-1 and y == 0:
        result.append(move_count)
        return
    before = graph[y][x]
    graph[y][x] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] != -1:
            dfs(nx, ny, move_count+1)
    graph[y][x] = before
dfs(startX, startY, 1)
print(result.count(K))