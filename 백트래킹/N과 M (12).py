N,M = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

s = []
def backtracking(num):
    if len(s) == M:
        print(*s)
        return
    prev = -1
    for i in range(N):
        if a[i]<num:
            continue
        if a[i] == prev:
            continue
        s.append(a[i])
        backtracking(a[i])
        prev = s.pop()
backtracking(a[0])