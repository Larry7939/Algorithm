def backtracking(index, s):
    if index == N:
        if len(s) == 6:
            print(*s)
        return
    
    backtracking(index+1, s + [path[index]])
    backtracking(index+1, s)

while True:
    p = list(map(int,input().split()))
    if p[0] == 0:
        break
    N = p[0]
    path = p[1:]
    s = []
    backtracking(0,s)
    print()