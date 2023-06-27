# BOJ 1138 한 줄로 서기
import sys

# 사람의 수
N = int(sys.stdin.readline())
# 본인보다 큰 사람이 왼쪽에 몇 명 있었는지에 대한 정보
info = list(map(int, sys.stdin.readline().split()))
answer = [0]*N
#외부 반복문에서 answer를 돌면서, 내부 반복문에서는 각 사람에 대해서 cnt가 info[i]와 일치하고, 빈 자리가 날 때까지 cnt를 증가시킨다.

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == info[i] and answer[j] == 0:
            answer[j] = i+1
            break
        elif answer[j] == 0:
            cnt += 1
print(*answer)