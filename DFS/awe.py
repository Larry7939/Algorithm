#입력부
n = int(input())#전체 사람의 수 N
x,y = map(int,input().split())#두 사람의 번호 x,y
m = int(input())#관계 개수 m
graph = [[] for _ in range(n+1)]
#m만큼 관계 입력
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
result = []
num = 0
#dfs
def dfs(v,num):
    visited[v] = True
    num += 1
    if v==y:
        result.append(num)
    for i in graph[v]:
        if not visited[i]:
            dfs(i,num)
    
#출력
#두 사람의 촌수 출력
dfs(x,num)
if len(result):
    print(result[0]-1)
else:
    print("awef")