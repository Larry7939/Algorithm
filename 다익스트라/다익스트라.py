import sys
input = sys.stdin.readline
INF = int(1e9) # 아직 연결되지 않은 노드에 대한 거리(10억)
n, m = map(int,input().split()) #n - 노드의 개수, m - 관계의 개수
start = int(input())
#주어지는 그래프 정보 담는 N개 길이의 리스트
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1) #방문처리 기록용 리스트
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split()) #출발지, 목적지, 거리
    graph[a].append((b,c))

#방문하지 않은 노드이면서 시작 노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if not visited[i] and distance[i]<min_value: #방문하지 않았고, 최단 거리인 곳
            min_value = distance[i]
            index = i
    return index

#다익스트라 알고리즘
def dijkstra(start):
    #시작 노드 -> 시작노드 거리 계산 및 방문처리
    distance[start] = 0 # 자기 자신과의 거리 0
    visited[start] = True 
    #시작 노드의 인접한 노드들에 대해 최단거리 계산 - 최초 업데이트
    for i in graph[start]:
        distance[i[0]] = i[1] #i[0]은 목적지, i[1]은 거리
    
    #시작 노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(n-1):
        now = get_smallest_node() #방문하지 않았고, 시작노드와 최단 거리인 노드 반환
        visited[now] = True #해당 노드 방문처리
        #해당 now 노드의 인접한 노드들 간의 거리 계산
        for next in graph[now]: #now 노드와 연결된 노드들의 거리 계산
            cost = distance[now] + next[1] #거리 총합 = now까지의 거리 + now와 연결된 노드의 거리
            if cost < distance[next[0]]: #만약 새로 구한 거리총합이 next까지 오는 데에 걸리는 거리 distance[next[0]]보다 작으면
                distance[next[0]] = cost #distance업데이트
dijkstra(start)
for i in range(1,n+1):
    if distance[i] == INF:
        print("도달할 수 없음")
    else:
        print(distance[i])
            





