# 풀이 횟수 3
import sys
input = sys.stdin.readline
# 모든 좌표에 대해서 dfs 호출하고 True를 반환하면 count 1증가
# 호출하는 과정에서 지나간 길을 전부 1로 만듦

dx = [0,0,-1,1]
dy = [-1,1,0,0]
answer = 0
#dfs
def dfs(x,y):
    if graph[y][x] == 0:
        graph[y][x] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx] == 0:
                    dfs(nx,ny)  #이 과정은 어차피 깊이우선탐색을 하면서 전부 1로 만들기 위한 것일 뿐이다.
        return True # graph[y][x]==0 이 순간부터 True반환은 확정된 것임.
# 입력
# 세로(N), 가로(M)
# 얼음틀
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().strip()))
for i in range(n):
    for j in range(m):
        if dfs(j,i):
            answer += 1

print(answer)