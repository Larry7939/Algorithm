n = int(input())
distances = list(map(int,input().split()))
visited = [False] * (len(distances)+1)
s = int(input())-1

# 현재 인덱스로부터 접근 가능한 곳, 즉, v + distances[v]가 조건(돌다리 밖으로 나가지 않게끔)을 만족하면 거기로 점프
def dfs(v):
    count = 1
    visited[v] = True
    # 두 방향 중 갈 수 있는 곳은 다 시도해본다
    if v + distances[v] < n and visited[v + distances[v]] == False:
        count += dfs(v + distances[v])
    if v - distances[v] >= 0 and visited[v - distances[v]] == False:
        count += dfs(v - distances[v])
    return count
result = dfs(s)
print(result)