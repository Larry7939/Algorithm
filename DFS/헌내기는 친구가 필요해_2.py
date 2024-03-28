# N X M 크기 캠퍼스에서 상하좌우 이동
# 캠퍼스 세로, 가로 길이 N, M 입력
import sys
sys.setrecursionlimit(10**7)
# O - 빈 공간
# X - 벽
# I - 도연이
# P - 사람

# 상하좌우 백터 만들기
# 도연이의 좌표 start 얻기
# dfs
#  한 번 간 곳은 X로 만들기
#  P 만나면 카운트
dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]

N,M = map(int,input().split())
graph = []
start = (0,0)
for i in range(N):
    row_list = list(input())
    if 'I' in row_list:
        start = (i,row_list.index('I'))
    graph.append(row_list)
person_count = [0]

def dfs(x,y):
    if graph[y][x] == 'P':
        person_count[0] += 1
    graph[y][x] = 'X'
    for i in range(4):
        if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N:
            if graph[y+dy[i]][x+dx[i]] != 'X':
                dfs(x+dx[i], y+dy[i])
dfs(start[1],start[0])
if person_count[0] == 0:
    print("TT")
else:
    print(person_count[0])
# 도연이가 캠퍼스에서 만날 수 있는 사람의 수 출력
