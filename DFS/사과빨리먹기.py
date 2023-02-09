import sys
BOARD_SIZE = 5
# BOJ 26170
# 개요
# 5X5크기의 보드
# 격자 - 사과가 1개(1), 장애물(-1) , 빈칸(0)
# r,c행렬
# 상하좌우 이동 가능
# 지나간 칸은 다시 지나갈 수 없음. visited = True

# 상하좌우 dx,dy정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(graph, x, y, answer, count, apple):
    # 사과가 3개면 answer.append(count)로 이동횟수 append
    if apple == 3:
        answer.append(count)
    # 반복문으로 dfs호출
    for i in range(4):
        # nx,ny에 현재 좌표 x,y를 더한 값 dx,dy만들기
        nx = x+dx[i]
        ny = y+dy[i]

        # 인덱스 검사(dx<0 or dx>BOARD_SIZE-1 or dy<0 or dy>BOARD_SIZE-1)를 충족하지 못하면 continue
        if nx < 0 or nx > BOARD_SIZE-1 or ny < 0 or ny > BOARD_SIZE-1:
            continue
        if graph[ny][nx] == -1:  # 해당 좌표가 -1 이라면 막혔으니 pass
            continue
        if graph[ny][nx] == 1:  # 1이라면 status를 True로 정해주고 apple의 수를 증가시킨다.
            status = True
            apple += 1
        else:
            status = False  # 0일 경우에는 status를 False로 한다.
        # dfs에서 빠져 나왔을 경우 road[x][y]의 값을 복귀시켜야 하기 때문에 변수에 저장시켜 놓는다.
        current = graph[y][x]
        graph[y][x] = -1
        dfs(graph, nx, ny, answer, count+1, apple)
        graph[y][x] = current  # 빠져나왔을 경우 좌표 값 원복
        if status == True:  # 만약 사과를 하나 챙겼다면 원복
            apple -= 1
    return answer


answer = []
apple = 0
graph = [[] for _ in range(BOARD_SIZE)]
for i in range(BOARD_SIZE):
    graph[i] = list(map(int, sys.stdin.readline().split()))
y, x = map(int, input().split())
answer = dfs(graph, x, y, answer, 0, apple)

if len(answer) == 0:
    print(-1)
else:
    print(min(answer))

# 핵심 아이디어 -> 사과를 3개 모을 수 있는 모든 경로를 가보고, 그 중 최소 이동 횟수를 출력한다.
# 한 경로를 끝까지 다녀올 때마다, 다녀온 길을 다시 돌아오면서 -1로 바꾼 것을 원래대로 0또는1로 원상 복구 시킨다.
# 다른 방향으로 호출할 때, 지나간 길로 되어있는 -1 길을 전부 원래대로 되돌려주기 위해서(빈 칸 또는 사과) current를 저장했다가 dfs호출을 마치고 나면 원복해주는 것임.
# 그리고 새로 다른 방향으로 갈 때에는 apple이 0이 되어있어야 할테니까, 그것도 status로 미리 다 치워주는 것이다.
