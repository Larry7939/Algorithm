# 기둥 - 바닥 위 or 보의 한쪽 끝 or 다른 기둥 위
# 보 - 한쪽 끝이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시 연결
# 벽 - n x n
# 기둥/보 삭제 기능 - 기둥과 보의 조건 불만족 시 무시
# n - 벽면의 크기
# build_frame - 기둥과 보 설치/삭제 작업 2차원 배열
# 모든 작업 수행 후 구조물의 상태 return
# build_frame[x,y,a,b]
#  x,y - 각각 기둥 보 설치/삭제 교차점의 가로/세로 좌표
#  a - 설치/삭제할 구조물의 종류 - 0:기둥, 1:보
#  b - 설치(1) or 삭제(0) 여부
#  바닥에는 보 설치 불가, 벽면을 벗어나서 설치하는 경우는 x
# 보는 좌표기준 오른쪽, 기둥은 위쪽 방향으로 설치, 삭제
# 겹치는 경우 x, 없는 구조물 삭제 x

# 0. 기둥과 보를 1로 정의
# 1. board_poll을 원소 0을 가진 nxn 크기의 2차원 배열로 초기화
# 2. board_barrage를 원소 0을 가진 nxn크기의 2차원 배열로 초기화
def createBoard(n):
    board_poll = [[0]*n for _ in range(n)]
    board_barrage = [[0]*n for _ in range(n)]
    return board_poll, board_barrage
def showPollBoard(n,board_poll):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end='')
        print()
def showBarrageBoard(n,board_barrage):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end='')
        print()
# 3. build_frame을 돌아가며 만약 b가 1(설치)이라면, 각각의 원소에 대해서 4번 동작을 수행
# 4. 만약 a가 0(기둥)이라면, 기둥 설치 조건을 만족하는 지를 체크
#    만약 a가 1(보)이라면, 보 설치 조건을 만족하는 지를 체크
#    불만족한다면 continue
#    만족한다면 각각 board_poll과 board_barrage의 (x,y)에 기둥 또는 보를 설치
# 기둥 - 바닥 위 or 보의 한쪽 끝 or 다른 기둥 위
# 보 - 한쪽 끝이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시 연결
#  바닥에는 보 설치 불가, 벽면을 벗어나서 설치하는 경우는 x
# 보는 좌표기준 오른쪽, 기둥은 위쪽 방향으로 설치, 삭제
# 겹치는 경우 x, 없는 구조물 삭제 x
def isBuildingPollEnable(x,y,board_poll,board_barrage): #허공에는 불가능
    if board_poll[y][x] != 1 or board_barrage[y][x] !=1 or y==0: #다른 기둥 위 or 보 위 or 바닥인 경우 설치 가능
        return True
    else:
        return False
def isBuildingBarrageEnable(n,x,y,board_poll,board_barrage)
    if  x-1 >= 0 and x+1<n and y-1 >= 0:
        if (board_poll[y][x] == 1 and board_poll[y-1][x] == 1) or (board_poll[y][x+1] == 1 and board_poll[y-1][x+1]) or (board_barrage[y][x-1]==1 and board_barrage[y][x+1] == 1) #한쪽 끝이 기둥 '위' or 양쪽 끝 부분이 다른 보와 동시 연결
            return True
    else:
        return False
def buildPoll(x,y,board_poll):
    board_poll[y][x] = 1
    board_poll[y+1][x] = 1
def buildBarrage(x,y,board_barrage):
    board_barrage[y][x] = 1
    board_barrage[y][x+1] = 1

# 3. build_frame을 돌아가며 만약 b가 0(삭제)이라면, 각각의 원소에 대해서 5번 동작을 수행
# 5. 만약 a가 0(기둥)이라면, 기둥 삭제 조건을 만족하는 지를 체크
#    만약 a가 1(보)이라면, 보 삭제 조건을 만족하는 지를 체크
#    불만족한다면 continue
#    만족한다면 각각 board_poll과 board_barrage의 (x,y)에 존재하는 기둥 또는 보를 삭제
#   기둥/보 삭제 기능 - 기둥과 보의 조건 불만족 시 무시
#   없는 구조물 삭제 x
#   삭제 후의 나머지 구조물들이 규칙에 어긋나면, 무시
def demolishPoll(x,y,board_poll):
    board_poll[y][x] = 0
    board_poll[y+1][x] = 0
def demolishBarrage(x,y,board_barrage):
    board_barrage[y][x] = 0
    board_barrage[y+1][x] = 0

def isDemolishingPollEnable(n,x,y,board_poll,board_barrage):
    result = False
    demolishPoll(x,y,board_poll)
    # 기둥의 머리 부분에 보나 기둥이 연결 점을 얻은 다음, 기둥 삭제 
    # 기둥의 경우 isBuildingPollEnable(x,y+1,board_poll,board_barrage)을 호출하고, 
    # 보의 경우, 기둥 머리 기준 왼쪽에만 있는 경우, 오른쪽에만 있는 경우, 둘 다 있는 경우를 분기처리해서 각각 isBuildingBarrageEnable(n,x,y,board_poll,board_barrage)호출
    #기둥 체크
    if y+2 < n:
        if board_poll[x,y+1] == 1 and board_poll[x,y+2] == 1:
            if isBuildingPollEnable(x,y+1,board_poll,board_barrage): result = True 
            else: result = False
    #왼쪽에만 있는 경우
    if y+1 < n:
        if x-1>=0:
            if board_barrage[y+1][x-1] ==1 and board_barrage[y+1][x] == 1: 
                if isBuildingBarrageEnable(n,x-1,y+1,board_poll,board_barrage): result = True else: return False
        if x+1<n:
        #오른쪽에만 있는 경우
            if board_barrage[y+1][x] ==1 and board_barrage[y+1][x+1] == 1: 
                if isBuildingBarrageEnable(n,x,y+1,board_poll,board_barrage): result = True else: return False
        if x-1 >=0 and x+1<n:
            #양쪽 모두 있는 경우
            if board_barrage[y+1][x-1] ==1 and board_barrage[y+1][x] == 1 and board_barrage[y+1][x+1] == 1: 
                if isBuildingBarrageEnable(n,x-1,y+1,board_poll,board_barrage) and isBuildingBarrageEnable(n,x,y+1,board_poll,board_barrage): result = True
                else: return False  
    # 전부 가능하면 원상복구(buildPoll(x,y,board_poll))를 시키고 Result에 True를 넣고 반환한다.
    buildPoll(x,y,board_poll)
    result = True
    return result

# 보를 없애고, 
# 좌측의 좌표에 기둥을 세울 수 있는지 체크
# 우측의 좌표에 기둥을 세울 수 있는지 체크
# 좌우의 좌표에 기둥을 세울 수 있는지 체크
# 좌측의 보를 만들 수 있는지 체크
# 우측의 보를 만들 수 있는지 체크
# 좌우의 보를 모두 만들 수 있는지 체크
def isDemolishingBarrageEnable(n,x,y,board_poll,board_barrage):
    demolishBarrage(x,y,board_barrage)
    
    
    
# 6. 결과는 board_poll에 존재하는 1의 x,y좌표에 0을 붙이고, board_barrage에 존재하는 1의 x,y좌표에 1을 붙여서, 
#    배열 answer에 append
def build(a,b,board_poll,board_barrage):
    for 

def solution(n, build_frame):
    board_poll, board_barrage = createBoard(n)

    
    
    answer = [[]]
    return answer