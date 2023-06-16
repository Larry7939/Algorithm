# 프로그래머스 기둥과 보 설치 24/100

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

# 기둥과 보의 위치를 2차원 배열상에서 0 또는 1로 나타내는 방식의 문제점 -> 보의 '시작'지점을 특정하기에는 코드가 지나치게 길어지고 까다로워짐
# 해결방법 => 1차원 배열 2개로 기둥과 보의 '시작'좌표를 튜플형태로 저장하는 방식

# 1. board_poll와 board_barrage를 빈 배열로 초기화
# 2. build_frame을 돌아가며 만약 b가 1(설치)이라면, 각각의 원소에 대해서 3번 동작을 수행
# 2. build_frame을 돌아가며 만약 b가 0(삭제)이라면, 각각의 원소에 대해서 4번 동작을 수행

# 3. 만약 a가 0(기둥)이라면, 기둥 설치 조건을 만족하는 지를 체크
#    만약 a가 1(보)이라면, 보 설치 조건을 만족하는 지를 체크
#    불만족한다면 continue
#    만족한다면 각각 board_poll또는 board_barrage에 (x,y)를 append

# 4. 만약 a가 0(기둥)이라면, 기둥 삭제 조건을 만족하는 지를 체크
#    만약 a가 1(보)이라면, 보 삭제 조건을 만족하는 지를 체크
#    불만족한다면 continue
#    만족한다면 각각 board_poll또는 board_barrage에서 (x,y)를 remove
def buildPoll(x,y,board_poll:list):
    board_poll.append((x,y))
def buildBarrage(x,y,board_barrage:list):
    board_barrage.append((x,y))

def demolishPoll(x,y,board_poll:list):
    if (x,y) in board_poll:
        board_poll.remove((x,y))
def demolishBarrage(x,y,board_barrage:list):
    if (x,y) in board_barrage:
        board_barrage.remove((x,y))
# 각 구조물의 유지 조건
#   기둥 - 바닥 위 or 보의 한쪽 끝 or 다른 기둥 위
#   보 - 한쪽 끝이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시 연결
#   바닥에는 보 설치 불가, 벽면을 벗어나서 설치하는 경우는 x
#   보는 좌표기준 오른쪽, 기둥은 위쪽 방향으로 설치, 삭제
#   겹치는 경우 x, 없는 구조물 삭제 x
def isBuildingPollEnable(x,y,board_poll:list,board_barrage:list):
    if y==0 or (x,y-1) in board_poll or (x,y) in board_barrage or (x-1,y) in board_barrage:
        return True
    else: 
        return False
def isBuildingBarrageEnable(x,y,board_poll:list,board_barrage:list):
    if (x,y-1) in board_poll or (x+1,y-1) in board_poll or ((x-1,y) in board_barrage and (x+1,y) in board_barrage): 
        return True
    else: 
        return False
def isDemolishingPollEnable(x,y,board_poll:list,board_barrage:list):
    demolishPoll(x,y,board_poll) #기둥이 사라진 상태를 가정
    if (x-1,y+1) in board_barrage: #기둥 머리에 보가 있는 경우(좌)
        if isBuildingBarrageEnable(x-1,y+1,board_poll,board_barrage) == False:
            buildPoll(x,y,board_poll) #원상복구
            return False
    if (x,y+1) in board_barrage: #기둥 머리에 보가 있는 경우(우)
        if isBuildingBarrageEnable(x,y+1,board_poll,board_barrage) == False:
            buildPoll(x,y,board_poll) #원상복구
            return False
    if (x,y+1) in board_poll: #기둥 위에 기둥이 있는 경우
        if isBuildingPollEnable(x,y,board_poll) == False:
            buildPoll(x,y,board_poll) #원상복구
            return False
    buildPoll(x,y,board_poll) #원상복구
    return True
    
def isDemolishingBarrageEnable(x,y,board_poll:list,board_barrage:list):
    demolishBarrage(x,y,board_barrage) #보가 사라진 상태를 가정
    #보의 끝에 보가 있는 경우(좌)
    if (x,y) in board_barrage:
        if isBuildingBarrageEnable(x,y,board_poll,board_barrage) == False:
            buildBarrage(x,y,board_barrage) #원상복구
            
            return False
    #보의 끝에 보가 있는 경우(우)
    if (x+1,y) in board_barrage:
        if isBuildingBarrageEnable(x+1,y,board_poll,board_barrage) == False:
            buildBarrage(x,y,board_barrage) #원상복구
            return False
    #보의 끝에 기둥이 있는 경우(좌)
    if (x,y) in board_poll:
        if isBuildingPollEnable(x,y,board_poll,board_barrage) == False:
            buildBarrage(x,y,board_barrage) #원상복구
            return False
    #보의 끝에 기둥이 있는 경우(우)
    if (x+1,y) in board_poll:
        if isBuildingPollEnable(x+1,y,board_poll,board_barrage) == False:
            buildBarrage(x,y,board_barrage) #원상복구          
            return False
    buildBarrage(x,y,board_barrage) #원상복구
    
    return True

def build(b,a,x,y,board_poll,board_barrage):
    if b == 0: #삭제
        if a == 0: #기둥
            if isDemolishingPollEnable(x,y,board_poll,board_barrage):
                demolishPoll(x,y,board_poll)
        elif a == 1: #보
            if isDemolishingBarrageEnable(x,y,board_poll,board_barrage):
                demolishBarrage(x,y,board_barrage)
                
    elif b == 1: #설치
        if a == 0: #기둥
            if isBuildingPollEnable(x,y,board_poll,board_barrage):
                buildPoll(x,y,board_poll)
        elif a == 1: #보
            if isBuildingBarrageEnable(x,y,board_poll,board_barrage):
                buildBarrage(x,y,board_barrage)
def getResult(answer,board_poll,board_barrage):
    for x,y in board_poll:
        answer.append([x,y,0]) #x,y,a 각각 좌표, 구조물 유형(기둥 - 0)
    for x,y in board_barrage:
        answer.append([x,y,1]) #x,y,a 각각 좌표, 구조물 유형(보 - 1)
    answer.sort()
    
def solution(n, build_frame):
    answer = []
    board_poll = []
    board_barrage = []
    for x,y,a,b in build_frame:
        build(b,a,x,y,board_poll,board_barrage)
    getResult(answer,board_poll,board_barrage)
    return answer
