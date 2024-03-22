#BOJ 11497 통나무 건너뛰기
from collections import deque
# 테스트 케이스의 수 T
# 통나무의 개수 N
# 통나무의 높이 리스트 L
T = int(input())
dq = deque([])
def getMaxDiff(dq:deque, N:int): 
    maxDiff = 0
    for i in range(1,N):
        maxDiff = max(maxDiff, abs(dq[i-1]-dq[i]))
    return maxDiff

for _ in range(T):
    N = int(input())
    L = list(map(int,input().split()))
    L.sort(reverse = True)
    dq.append(L[0])
    for i in range(1,N):
        if i % 2 != 0:
            dq.appendleft(L[i])
        else:
            dq.append(L[i])
    print(getMaxDiff(dq, N))
    dq.clear()

# deque을 만들어놓고 가장 큰 것의 양 옆으로 append와 appendleft 반복
# 만들어진 deque의 맨 앞부터 뒤의 원소와의 차이를 구해가며, 가장 큰 차이를 구해나간다.
# 해당 차이를 출력한다.