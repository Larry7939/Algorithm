N, M =map(int,input().split())

a = list(map(int,input().split()))

a.sort()

s = []
visited = [False] * N

def backtracking():
    if len(s) == M:
        print(*s)
        return
    prev = -1
    for i in range(N):
        if visited[i]:
            continue
        if prev == a[i]:
            print("prev->",prev)
            continue
        visited[i] = True
        s.append(a[i])
        backtracking()
        prev = s.pop()
        visited[i] = False
backtracking()