import sys
COLUMN_SIZE, ROW_SIZE = map(int, sys.stdin.readline().split())
y, x, d = map(int, sys.stdin.readline().split())
directions = [0, 3, 2, 1]  # 북/서/남/동
direction = directions[d]
dx = [0,-1,0,1] # 북/서/남/동
dy = [-1,0,1,0] # 북/서/남/동
graph = []
for _ in range(COLUMN_SIZE):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
# 1 방향 정하기
# 2 회전 후 한칸 전진
# 3 가본 칸이거나 바다로 되어있는 경우, 방향 유지, 한칸 뒤로, 1단계로 돌아가기. but, 뒤가 바다라면 움직임 멈춤
answer = 1
graph[y][x] = 1
is_enable = False
def rotateLeftDirection():
    global direction
    global d
    d = (d+1)%3
    direction = directions[d]

while True:
    for i in range(len(dx)):
        nx,ny = x+dx[i], y+dy[i]
        rotateLeftDirection()
        if nx<0 or nx > ROW_SIZE-1 or ny<0 or ny>COLUMN_SIZE-1 or graph[ny][nx] == 1:
            is_enable = False
            continue
        else:
            graph[ny][nx] = 1
            x,y = nx,ny
            answer += 1
            is_enable = True
            break
    if is_enable == False:
        nx = x - dx[d]
        ny = y - dy[d]
        if nx<0 or nx > ROW_SIZE-1 or ny<0 or ny>COLUMN_SIZE-1 or graph[ny][nx] == 1:
            break
        else:
            x = nx
            y = ny
print(answer)
#왼쪽 방향부터 차례대로 갈 곳을 정한다.
#검사 - nx,ny가 x,y를 넘어가지 않고, graph[y][x] != 1인 조건
# a - 통과한다면, 회전하고 한칸 전진
# b - 통과하지 못한다면, 다시 왼쪽 회전(continue)
# 네 방향 모두 바다 or 가본 칸인 경우(1인 경우), 방향유지 후 뒤로 1칸
# a - 뒤 쪽도 바다라면 움직임 종료
# b - continue
