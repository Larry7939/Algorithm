import sys
n = int(sys.stdin.readline())
plans = list(sys.stdin.readline().split())

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['U', 'D', 'L', 'R']
for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx, ny = x+dx[i], y+dy[i]
    if nx<1 or nx > n or ny < 1 or ny > n:
        continue
    else:
        x,y = nx,ny
print(y,x)