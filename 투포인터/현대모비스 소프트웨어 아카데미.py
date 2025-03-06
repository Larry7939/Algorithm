# N(학회원의 수), M(팀 최소 능력치) 입력
# stats[] 학회원 능력치 정수 리스트
# result 구성 가능한 팀의 수
N, M = map(int, input().split())
stats = list(map(int,input().split()))
checked = [False] * N
result =0

# [조건]
# 1. 구성이 안 되어있어야 함(checked[index]가 False])
# 2. 두 수의 합이 M 이상이어야함.

# 1. stats 오름차순 정렬
stats.sort()
# 2. 투포인터를 활용하여 low, high 두 인덱스를 증가/감소 시킨다.
# stats[low] + stats[high]가 M 미만일 때, low 증가
# stats[low] + stats[high]가 M 이상일 때, result += 1, low 증가, high = N-1,

low = 0
high = N-1
while low < high:
    if stats[low] + stats[high] < M:
        low += 1
    else:
        result += 1
        low += 1
        high -= 1
        
print(result)

# 핵심: 투포인터를 이해하고 있는가