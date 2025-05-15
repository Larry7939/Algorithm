#BOJ 2664 촌수계산
# 풀이 횟수 5

#입력부
#N - 전체 사람의 수 (1<=N<=100)
#a,b - 촌 수를 계산할 서로 다른 두 사람의 번호
#M - 부모자식들 간의 관계의 개수
#x(부모),y(자식) - 부모자식간의 관계 M번 입력
n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

#상하관계가 아니라 연결 관계로 보기!
#graph[i]을 통해 특정 사람 i와 연결된 사람들을 전부 볼 수 있도록 함
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False]*(n+1)
num = 0
result = []
#dfs 정의
def dfs(v,num):
#매번 num +1 및 visited[v] = True
    num += 1
    visited[v] = True
#만약 v가 b와 같으면, return num
    if v==b:
        result.append(num)
#for문으로 graph[v]를 돌면서, 연결된 모든 녀석들에 대해서 dfs호출
    for i in graph[v]:
        if not visited[i]:
            dfs(i,num)

#dfs호출
dfs(a,num)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)