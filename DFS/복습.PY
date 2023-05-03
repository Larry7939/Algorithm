# 입력
# 전체 사람의 수 : N
# 촌수 계산 대상 : a,b
# 관계의 수 : M
# 관계 M 개

N = int(input())
a, b = map(int, input().split())
M = int(input())
relationship = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    x, y = map(int, input().split())
    relationship[x].append(y)
    relationship[y].append(x)
num = 0
result = []

# 입력받은 두 사람의 번호를 양방향으로 연결
# dfs로 a부터 시작해서 b가 나올 때까지 answer를 증가시키며 재귀호출
# for문으로 relationship[]을 전부 돌면서 체크
# if문으로 visited여부 체크
# if문으로 v가 b가 맞으면, isMatched를 True로 변경
# 출력부
# isMatched가 False면 -1, True면 answer 출력


def dfs(v,num):
    num+=1 #global을 사용하면 안되는 이유 - 다른 분기를 거친 결과가 num에 누적되어버리기 때문
    visited[v] = True
    if (v == b):
        result.append(num)
    for i in relationship[v]:
        if visited[i] == False:
            dfs(i,num)
dfs(a,num)
if len(result)==0:
    print(-1)
else:
    print(result[0]-1)