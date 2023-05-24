#숫자 카드 게임
#N,M
N,M = map(int,input().split())
board = [[] for _ in range(N)]
for n in range(N):
    temp = list(map(int,input().split()))
    board[n] = temp

#각 행 중에서 최솟값을 뽑은 다음 비교,
a = []
for i in board:
    a.append(min(i))
print(max(a))

