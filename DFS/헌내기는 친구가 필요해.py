# BOJ 21736
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# O(빈 칸), X(벽), I(도연이), P(사람)
# I는 단 한번만 주어진다.

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
# dfs
def dfs(x, y,visited):
    global answer
    if graph[y][x] == 'P':
        answer+=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
            continue
        if graph[ny][nx] == 'X':
            continue
        visited[y][x] = True
        if visited[ny][nx]==False:
            dfs(nx,ny,visited)

# 입력1
# 캠퍼스의 크기 1<=N,M<=600
# N개의 줄만큼의 캠퍼스 정보
N, M = map(int, input().split())
visited = [[False]*M for _ in range(N)]
num = 0
graph = []
for i in range(N):
    graph.append(input())

# 도연이 위치 찾기
for i in range(N):
    if 'I' in graph[i]:
        x, y = (graph[i].find('I'),i)
        
dfs(x, y,visited)

if answer == 0:
    print("TT")
else:
    print(answer)

# 정답 answer
# dfs==True - answer 출력
# dfs==False - "TT"출력
