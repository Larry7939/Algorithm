#BOJ 5212 지구 온난화
import sys

# 'X'는 땅, '.'는 바다를 나타낸다.
# 50년 후, 인접한 3칸 혹은 4칸에 바다가 있는 땅은 모두 잠긴다.(바다가 된다.)
# 출력 - 50년 후의 지도(한 행에 적어도 하나의 땅을 포함하고 있어야 함)
def showBoard(board):
    #땅이 발견된 x,y좌표중 최솟값, 최댓값
    x_min = R 
    x_max = 0
    y_min = C
    y_max = 0 
    for i in range(C):
        for j in range(R):
            if 'X' in board[i][j]:
                x_min = min(x_min,j)
                x_max = max(x_max,j)
                y_min = min(y_min,i)
                y_max = max(y_max,i)
    for i in range(y_min,y_max+1):
        for j in range(x_min,x_max+1):
            print(board[i][j],end='')
        print()
def checkLand(board,x,y):
    cnt = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>R-1 or ny<0 or ny>C-1: #지도에 나타난 영역 외부는 전부 바다
            cnt += 1
            continue
        else:
            if board[ny][nx] == '.':
                cnt += 1
    if cnt >= 3:
        return True
    else:
        return False

board =[]
#입력
#다도해의 지도 크기
C,R = map(int,sys.stdin.readline().split())
for _ in range(C):
    row = list(sys.stdin.readline().rstrip())
    board.append(row)
#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
lands_to_convert = []
#완전탐색으로 땅이 나올 때, 땅을 둘러싼 4 방향이 바다인지를 체크하고, True라면 해당 땅의 좌표를 따로 append
#전부 끝난 후, append된 좌표의 땅만 바다('.')로 변경
for i in range(C):
    for j in range(R):
        if board[i][j] == 'X':
            if checkLand(board,j,i):
                lands_to_convert.append((j,i))

for land in lands_to_convert:
    board[land[1]][land[0]] = '.'
showBoard(board)
