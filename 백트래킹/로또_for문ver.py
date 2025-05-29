
def backtracking(num):
    if len(s)==M:
        print(*s)
        return
    for i in range(N):
        if visited[i]:
            continue
        if a[i] < num:
            continue
        visited[i] = True
        s.append(a[i])
        backtracking(a[i])
        s.pop()
        visited[i] = False 
        
while True:
    case = list(map(int,input().split()))
    if case[0] == 0:
        break
    else:
        N = case[0]
        a = case[1:]
        M = 6
        visited = [False]*N
        s = []
        backtracking(a[0])
        print()