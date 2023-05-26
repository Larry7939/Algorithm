<<<<<<< Updated upstream
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

=======
N, K = map(int, input().split())

# N이 K의 배수가 될 때 까지 뺀 다음 나누는 과정 필요
count = 0

while N != 1:
    if N % K != 0:
        N -= 1
        count += 1
        print(f"N={N} 뺄셈 연산")
    else:
        N = N//K
        count += 1
        print(f"N={N} 나눗셈 연산")
print(count)
>>>>>>> Stashed changes
