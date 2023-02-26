import sys
import heapq
#풀이횟수 2회
input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))  # 시작 노드 정보를 우선순위 큐에 삽입
    distance[start] = 0  # 시작노드 거리(자기 자신과의 거리) = 0
    while q:
        node, dist = heapq.heappop(q)
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if dist > distance[node]:
            continue
        # 큐에서 뽑아낸 거리가 기존에 기록된 거리 distance보다 작으면, 해당 노드와 인접 노드들의 거리를 업데이트 해준다.
        # 큐에서 뽑아낸 노드와 연결된 인접 노드들 탐색
        for next in graph[node]:
            # 새로 구한 총 거리 cost = 시작 -> node 거리 + node -> node의 인접노드 거리
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:  # cost < 시작 -> node의 인접 거리
                distance[next[0]] = cost
                heapq.heappush(q, (next[0], cost))
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