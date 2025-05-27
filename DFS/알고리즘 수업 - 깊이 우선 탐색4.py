import sys
sys.setrecursionlimit(10**7)

N,M,R = map(int,input().split())
# N: 정점의 수
# M: 간선의 수
# R: 시작 정점

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort(reverse=True)
    
result = [-1]*(N+1)
def dfs(v, count):
    visited[v] = True
    result[v] = count
    for g in graph[v]:
        if visited[g] == False:
            dfs(g, count +1)

dfs(R, 0)

for i in range(1,N+1):
    print(result[i])