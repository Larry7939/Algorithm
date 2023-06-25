#BOJ 5212 지구 온난화
import sys

# 'X'는 땅, '.'는 바다를 나타낸다.
# 50년 후, 인접한 3칸 혹은 4칸에 바다가 있는 땅은 모두 잠긴다.(바다가 된다.)
# 출력 - 50년 후의 지도(한 행에 적어도 하나의 땅을 포함하고 있어야 함)
def showBoard(board):
    for i in range(R):
        for j in range(C):
            print(board[i][j],end='')
        print()
def DFS():

board =[]
#입력
#다도해의 지도 크기
R,C = map(int,sys.stdin.readline().split())
for _ in range(5):
    row = sys.stdin.readline()
    board.append(row)

# board의 모든 좌표에 대해 x,y좌표와 board를 매개변수로 하는 dfs를 실행
# 내부에서는 땅의 3면 이상이 바다인지를 체크한다.
#  True인 경우 - '.'으로 변경
