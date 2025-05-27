import sys
sys.setrecursionlimit(10**7)

N, M, K = map(int,input().split())
# 친구의 수 N
# 도로의 수 M
# 여행을 떠난 친구의 수 K

graph = [[] for _ in range(N+2)]
visited = [False]* (N+2)
for _ in range(M):
    p, q = map(int,input().split())
    graph[p].append(q)
    graph[q].append(p)
locked = list(map(int,input().split()))

result = []
def dfs(v, count):
    visited[v] = True
    result.append(count)
    for a in graph[v]:
        if a not in locked and visited[a] == False:
            dfs(a, count + 1)
dfs(1,0)
print(len(result)-1)