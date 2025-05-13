# BOJ 2606 바이러스
# 풀이횟수 4회
# 컴퓨터의 수 입력
N = int(input())
# 쌍의 수 입력
M = int(input())
# 한 번에 한 쌍씩 입력
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x) #"서로 연결" -> 양방향이기 때문에, 반대로도 이어줘야함
visited = [False]*(N+1)
num = 0
result=[0]

def dfs(v, num):
    # visited = true
    # num += 1
    # 반복문 N
    # 만약 visited[i]가 true가 아니라면
    # dfs(v,num)
    visited[v] = True  # 방문 처리
    result[0] += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)
dfs(1, num)
print(result[0]-1)
