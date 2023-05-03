# 단방향 그래프
# 입력
#  작업 개수 - N
#  작업 순서 정보의 개수 - M
#  작업 순서 정보 - jobs[[]*N+1]
#  필수 작업 X
# 출력
#  X를 마치기 위한 사전 작업의 개수

N,M = map(int,input().split())
visited = [False]*(N+1)
jobs = [[] for _ in range(N+1)]
answer = 0

#입력할 때에는 사전 작업으로 거슬러 올라가야하기 때문에,
# jobs[y].append(x)
for _ in range(M):
    x,y = map(int,input().split())
    jobs[y].append(x)
X = int(input())

def dfs(v):
    global answer
    # visited true로 변경
    # for문으로 jobs[v]를 돌면서 if문으로 visited[i]검사
    # visited[i]가 False인 경우만 dfs(i), answer+=1
    visited[v] = True
    for i in jobs[v]:
        if visited[i] == False:
            answer+=1
            dfs(i)
dfs(X)
print(answer)