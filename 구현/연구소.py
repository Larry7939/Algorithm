#BOJ 14502 연구소
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
N,M = map(int,sys.stdin.readline().split())
initial_board = []
board = []
points = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(N):
    initial_board.append(list(map(int,sys.stdin.readline().split())))
def showBoard(board):
    for i in range(N):
        for j in range(M):
            print(board[i][j],end=' ')
        print()
# 바이러스의 확산과 벽 건축 이전으로 원상복구하는 로직:
def restore():
    return deepcopy(initial_board)
#  initial_board, board
# 벽 3개를 세우는 로직:
#  0인 모든 좌표를 구하고, 조합을 이용해 이 중에서 3개를 뽑아서 벽을 세운다.
def getPointsToConstruct(board:list):
    points = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                points.append((j,i))
    return list(combinations(points,3))
def construct(board:list,point:list):
    for p in point:
        x = p[0]
        y = p[1]
        board[y][x] = 1
# 바이러스를 퍼뜨리는 로직:
#  바이러스 시작지점으로부터 bfs를 활용하여 퍼뜨리기
def spread(board,x,y):
    dq = deque([])
    dq.append((x,y))
    while len(dq) != 0:
        x,y = dq.pop()
        board[y][x] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>M-1 or ny<0 or ny>N-1 or board[ny][nx] == 1 or board[ny][nx] == 2:
                continue
            else:
                dq.append((nx,ny))
def getVirusStartPoint(board:list):
    start = []
    for y in range(N):
        for x in range(M):
            if board[y][x] == 2:
                start.append((x,y))
    return start
# 안전 영역의 크기를 세는 로직
def getSafeArea(board:list):
    result = 0
    for y in range(N):
        result += board[y].count(0)
    return result



points_to_contruct = getPointsToConstruct(initial_board)
virus_start_point = getVirusStartPoint(initial_board)
answer = []
#이하의 과정을 벽 3개의 경우의 수만큼 반복한다.
for point in points_to_contruct:
    # 1. 최초 입력받은 상태로 원상복구한다.
    board = restore()
    # 2. 벽을 3개 세운다. 
    construct(board,point)
    # 3. 바이러스를 퍼뜨린다.
    for p in virus_start_point:
        spread(board,p[0],p[1])
    # 4. 안전 영역의 크기를 센 후, answer 배열에 넣는다.
    answer.append(getSafeArea(board))
    # print(point)
    # showBoard(board)
print(max(answer))

# 벽을 세우기 위한 모든 경우의 수를 따질 수 있어야 한다.
# 바이러스를 퍼뜨리기 위한 BFS 구현 및 각 로직의 순서를 미리 잘 설계하고 구성하는 것이 핵심!