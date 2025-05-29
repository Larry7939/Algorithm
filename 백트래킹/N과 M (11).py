N, M = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
s = []

def backtracking():
    if len(s) == M:
        print(*s)
        return
    prev = -1
    for i in range(N):
        if prev == a[i]:
            continue
        s.append(a[i])
        backtracking()
        prev = s.pop()
backtracking()