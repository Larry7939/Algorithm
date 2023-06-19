#BOJ 2563 색종이
import sys
# 색종이가 도화지 밖으로 나가는 경우는 없음
# answer = 색종이를 전부 붙인 후, 색종이가 붙은 영역의 넓이
# 1. 가로 100, 세로 100 크기의 2차원 배열을 만든다.
# 2. 입력받은 x,y부터 x+area까지, y부터 y+area까지 전부 1로 만든다.
# 3. 2차원 배열을 돌면서 1인 원소의 개수를 센다. -> print(answer)

n = int(sys.stdin.readline()) # 색종이의 수 n<=100
board_size = 100
board = [[0]*board_size for _ in range(100)]
area = 10
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split()) # x - 색종이와 도화지의 왼쪽 변 사이의 거리 , y - 색종이와 도화지의 아래쪽 변 사이의 거리
    for i in range(y,y+area):
        for j in range(x,x+area):
            board[i][j] = 1
answer = 0
for i in range(board_size):
    answer += board[i].count(1)
print(answer)