import heapq
n,m = map(int,input().split())
start = int(input())
INF = int(1e9)
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a,b,c = list(map(int,input().split()))
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(start,0))
    while q:
        node, dist = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(next[0],cost))
dijkstra(start)
for i in range(1,len(distance)):
    if distance[i] == INF:
        print("도달할 수 없음")
    else:
        print(i," - ", distance[i])

# 테스트 케이스
# 5 5
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 4 3 3
# 4 5 1