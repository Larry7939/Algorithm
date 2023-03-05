from collections import deque
#풀이횟수 1

#맨 처음에는 queue에 있는 것을 꺼내면서 시작
#queue에서 꺼내면, 그곳으로 이동하는 것임.
#queue가 비어있게 되면 실행 종료
#maze의 상하좌우를 검사해서 1인 곳이 있으면, queue에 삽입

n,m= map(int,input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

dx = [0,0,-1,1]#상하좌우
dy = [-1,1,0,0]


def bfs(x,y):
    queue = deque()
    queue.append((y,x))

    while queue:
        y,x = queue.popleft()
        print(f"y={y},x={x}")

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i] #x,y에 상하좌우에 해당하는 이동값을 넣어본다.

            if nx<0 or ny<0 or nx>=m or ny>=n: #실험값이 맵을 이탈하면 continue
                continue
            if maze[ny][nx] == 0: #괴물이 있는 공간이면 continue
                continue
            if maze[ny][nx]==1:
                maze[ny][nx] = maze[y][x]+1
                queue.append((ny,nx))
    return maze[n-1][m-1]

print(bfs(0,0))

for i in range(n):
    for j in range(m):
        print(maze[i][j],end=' ')
    print()
