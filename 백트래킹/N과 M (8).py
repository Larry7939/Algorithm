N, M =map(int,input().split())

a = list(map(int,input().split()))
a.sort()
s = []

def backtracking(num):
    if len(s) == M:
        print(*s)
        return
    for i in range(num, N):
        if num<=i: 
            s.append(a[i])
            backtracking(i)
            s.pop()
backtracking(0)