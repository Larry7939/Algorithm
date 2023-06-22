#BOJ 1913 달팽이
#메모리 - 70168KB
#시간 - 852mx
import sys
#n=3 -> 3+3+3+2+1 -> 5
#n=4 -> 4+4+4+3+3+2+1 -> 7
#n=5 -> 5+5+5+4+4+3+3+2+1 -> 9
#n=6 -> 6+6+6+5+5+4+4+3+3+2+1 -> 11
#n=7 -> 7+7+7+6+6+5+5+4+4+3+3+2+1 -> 13


# n만큼 이동 -> 3번 -> 아래,오른쪽,위
# n-1 ~~ 3만큼 이동 -> 2번 -> 왼쪽,아래 / 위, 왼쪽
# 2 -> 1번 -> 
# 1 -> 1번

#하우상좌 - 하우상좌 - 하우상좌



#보드 크기 입력
n = int(sys.stdin.readline())
#찾고자 하는 값 입력
value = int(sys.stdin.readline())
#0으로 초기화된 nxn 표 생성
def createBoard(n):
    board = [[0]*n for _ in range(n)]
    return board
def move(num,distance,board,direction,x,y):
    if direction == 0: #하
        for i in range(distance):
            board[y][x] = num
            if i == distance-1:
                break
            y+=1
            num -=1
    elif direction == 1: #우
        for i in range(distance):
            board[y][x] = num
            if i == distance-1:
                break
            x+=1
            num -=1
    elif direction == 2: #상
        for i in range(distance):
            board[y][x] = num
            if i == distance-1:
                break
            y-=1
            num -=1
    elif direction == 3: #좌
        for i in range(distance):
            board[y][x] = num
            if i == distance-1:
                break
            x-=1
            num -=1
    return num,x,y
def showBoard(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print()
def findPoint(x,board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == x:
                print(i+1,j+1)
                return



# 외부 반복문 n번 반복
# 내부 반복문 분기 처리 - 매번 방향 전환



#move에서는 전달된 distance만큼 x,y를 변경하며 board 세팅
#초기 방향 정의
direction = 0 #하
board = createBoard(n)
x,y = 0,0
num = n*n
for distance in range(n,0,-1):
    if distance == n:
        for _ in range(3): # n - move함수 3번 호출
            num,x,y = move(num,distance,board,direction,x,y)
            direction = (direction+1)%4
        
    elif distance == 2: # 2 - 1번
        num,x,y = move(num,distance,board,direction,x,y)
        direction = (direction+1)%4

    else:
        for _ in range(2): # n-1 ~ 3 - 2번
            num,x,y = move(num,distance,board,direction,x,y)
            direction = (direction+1)%4

board[n//2][n//2] = 1
showBoard(board)
findPoint(value,board)