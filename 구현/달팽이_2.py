import sys
#메모리 - 70180KB
#시간 - 968ms
# 한 방향당 한번에 움직이는 거리의 패턴을 파악하는 것이 핵심
def showBoard(board,value):
    x,y = 0,0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == value:
                x,y = i+1,j+1
            print(board[i][j],end=' ')
        print()
    print(x,y)
# 중심으로부터 시계방향으로 돌며 나오기
# 회전의 순서 - 상우하좌 + 상(마지막)
# 크기 입력
n = int(sys.stdin.readline())
# 찾고자 하는 값 입력
value = int(sys.stdin.readline())
#초기 좌표 및 방향
cur_row, cur_col = (n//2, n//2)
cur_d = 0
#board 세팅
board = [[0]*n for _ in range(n)]
board[cur_col][cur_row] = 1
# 상우하좌 해시맵 구현
directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
# moves 배열 구현
moves = []
#n까지 증가하는 num
num = 1
# n = 5 -> 1,1,2,2,3,3,4,4,5,5,5
for i in range(1, n):
    moves += [i]*2
moves.append(n-1)

for move in moves:
    for distance in range(move):
        num+=1
        cur_row += directions[cur_d][0]
        cur_col += directions[cur_d][1]
        board[cur_col][cur_row] = num
    cur_d = (cur_d + 1) % 4
showBoard(board,value)


