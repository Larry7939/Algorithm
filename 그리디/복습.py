import sys
# 볼링공 고르기
n,m = map(int,sys.stdin.readline().rstrip().split())
balls = list(map(int,sys.stdin.readline().rstrip().split()))
balls.sort()
answer = 0

# 1 2 2 3 3
# 1, 2, 2
# 매 공마다, 더 높은 무게들의 개수만큼 더해준다.
weight_list = [0]*(m+1)
for i in range(1,m+1):
    weight_list[i] = balls.count(i)

for i in range(1,m+1):
    n -= weight_list[i]
    answer += weight_list[i] * n
    
print(answer)