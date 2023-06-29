#BOJ 14719 빗물
import sys
#입력
# 2차원 세로길이 H, 가로길이 W
H,W = map(int,sys.stdin.readline().split())
# W개의 블록이 쌓인 높이(맨 왼쪽부터 차례대로)
blocks = list(map(int,sys.stdin.readline().split()))
board = [[0]*W for _ in range(H)]
answer = 0 #고이는 빗물의 총량
def showBoard():
    for i in range(H):
        for j in range(W):
            print(board[i][j],end='')
        print()
#둘째줄 입력을 참고하여 2차원 배열 board에 블록 쌓기
def setBlocks():
    for i in range(W):
        for j in range(H-blocks[i],H):
            board[j][i] = 1
#board를 돌며 물이 고여도 괜찮은 곳인지 체크하는 로직
def checkImpoundEnable(x,y):
    global answer
    left_block=False
    right_block=False
    for i in range(0,x):
        if board[y][i] == 1:
            left_block = True
    for i in range(x,len(board[y])):
        if board[y][i] == 1:
            right_block = True
    if left_block and right_block:
        board[y][x] = 2
        answer += 1
        return True
    else:
        return False

# - 좌우를 끝까지 검사하여, 벽이 있는지 체크 left,right 모두 True여야 물이 고일 수 있음

setBlocks()
for i in range(H):
    for j in range(W):
        if board[i][j] != 1:
            checkImpoundEnable(j,i)
#출력
#고이는 빗물의 총량
print(answer)
