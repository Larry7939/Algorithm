from collections import deque

M,N = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(M)]
dx = [0,0,-1,1,-1,-1,1,1] #상하좌우 좌상 좌하 우상 우하
dy = [-1,1,0,0,-1,1,-1,1]

cnt = 0

def bfs(x,y):
    dq = deque()
    dq.append([x,y])
    while dq:
        x,y = dq.popleft()
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[ny][nx]==1:
                dq.append([nx,ny])
                graph[ny][nx] = 0 #0으로 변경하는 부분을 if 밖에서 남발하면 시간초과 발생

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(j,i)
            cnt += 1
print(cnt)
#2중 for문으로 1인 것에 대해서만 bfs 호출
#bfs는 연결된 1을 전부 0으로 만들어주는 용도이고 일단 graph[i][j]가 1인 순간부터 cnt는 올라간다.