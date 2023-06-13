import sys
row_locations = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
start = sys.stdin.readline().rstrip()
x = row_locations.index(start[0])
y = int(start[1])
SIZE = 8
# 현재 위치는 배열로 받기 [0,a,b,c,~~,h]
# 상좌, 상우, 하좌, 하우, 좌상, 좌하, 우상, 우하
# 정의 후에, len(dx)를 돌면서, 현재 위치에서 이동 한 값을 nx,ny에 저장하고 검사하기!
# 유효하면 answer + 1, 유효하지 않으면 continue
dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, -1, -1, 1]

answer = 0
for i in range(len(dx)):
    nx, ny = x + dx[i], y + dy[i]
    if 0 < nx < SIZE+1 and 0 < ny < SIZE+1:
        answer += 1

print(answer)
