N, M = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
s = []
visited = [False] * N
def backtracking(num):
    if len(s) == M:
        print(*s)
        return
    prev = -1
    for i in range(N):
        if a[i] == prev:
            continue
        
        if a[i] >= num and visited[i] == False:
            visited[i] = True
            s.append(a[i])
            backtracking(a[i])
            prev = s.pop()
            visited[i] = False
backtracking(a[0])