#BOJ 3190 뱀
from collections import deque
import sys
# 보드크기 N
# 사과의 개수 K
# K줄의 행, 열
# 방향 변환 횟수 L
# L줄의 방향 변환 정보 X(초),C(L or D)

def createBoard(N):
    return [[0]*N for _ in range(N)]
def showBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end='')
        print()
def setApples(board,x,y):
    board[y][x] = 1

def checkGameOver(x,y,N,dq):
    if (x,y) in dq or x <0 or x >= N or y < 0 or y>=N: #본인 몸 또는 벽에 부딫히면 게임 종료
        return True

def move(direction,board,dq:deque):
    x,y = dq[0][0],dq[0][1]
    if direction == 'R':
        nx,ny = x+1,y
    elif direction == 'D':
        nx,ny = x,y+1
    elif direction =='L':
        nx,ny = x-1,y
    elif direction =='U':
        nx,ny = x,y-1
    # print(f"nx: {nx} ny: {ny}")
    if checkGameOver(nx,ny,N,dq):
        # print("종료")
        return False
    else:
        if board[ny][nx] == 1:  #사과가 있으면
            # print("사과 섭취")
            board[ny][nx] = 0  #사과 사라짐
            dq.appendleft((nx,ny)) # 머리 이동
        else: #사과가 없으면
            dq.appendleft((nx,ny)) # 머리 이동
            dq.pop() #꼬리 이동


def rotate(rotation,direction):
    if rotation == 'L':
        direction = (direction - 1)
        if direction == -1:
            direction = 3

    elif rotation == 'D':
        direction = (direction + 1)%4
    return direction

N = int(sys.stdin.readline())
board = createBoard(N)
K = int(sys.stdin.readline())
for _ in range(K):
    apple_colum,apple_row  = map(int,sys.stdin.readline().split())
    setApples(board, apple_row-1,apple_colum-1)
# showBoard(board)
plans = dict()
L = int(sys.stdin.readline())
for _ in range(L):
    x,c = sys.stdin.readline().split()
    plans[x] = c # ex - ('8' :'D', '10' : 'D', '11', 'D', '13', 'L')


time = 0
directions = ['R','D','L','U']
direction = 0 #우측
dq = deque([])
dq.appendleft((0,0))

while True:
    if move(directions[direction],board,dq) == False:
        print(time+1)
        break
    time+=1
    if str(time) in plans.keys():
        # print("방향 전환")
        rotation = plans[str(time)]
        direction = rotate(rotation,direction)
    # print(f"time:{time} dq:{dq}")
# 시뮬레이션
# 무한 반복
# 머리와 꼬리 위치 정보 저장 - 항상 
# 방향 변환 정보를 체크하여 한 칸 이동(최초에는 오른쪽 기본값) - 머리 이동
# deque에 머리 이동 위치가 들어있는지 체크 - True면 종료
# 이동한 칸에 사과가 있으면 방향에 따라 머리 이동
#                   없으면 꼬리 이동
# 시간 증가
# 꼬리가 머리를 따라가게 하는 방법 
# - deque을 활용
# - 매번 머리와 꼬리 위치를 배열에 넣고 빼기. 

# 모듈화 및 동작 순서를 잘 체크하는 것, deque를 활용하여 머리부터 꼬리까지의 인덱스를 저장하고 빼는 것이 핵심