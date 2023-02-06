# 풀이 횟수 2
# 모든 좌표에 대해서 dfs 호출하고 True를 반환하면 count 1증가
# 호출하는 과정에서 지나간 길을 전부 1로 만듦
result = 0
n, m = map(int, input().split())
graph = [[] for _ in range(m) for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input()))


def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(x, y-1)  # 상
        dfs(x, y+1)  # 하
        dfs(x-1, y)  # 좌
        # 우  #이 과정은 어차피 깊이우선탐색을 하면서 전부 1로 만들기 위한 것일 뿐이고, 결국에는 나중에는 False를 반환하게 되어있다.
        dfs(x+1, y)
        return True  # graph[y][x]==0 이 순간부터 True반환은 확정된 것임.
    return False


for y in range(n):
    for x in range(m):
        if dfs(x, y) == True:
            result += 1
print(result)
