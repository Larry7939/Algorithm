n = int(input())
MAP_SIZE = 19
MAP = [[0]*MAP_SIZE for _ in range(MAP_SIZE)]
for i in range(n):
    (y,x) = map(int,input().split())
    MAP[y-1][x-1] = 1

for j in range(MAP_SIZE):
    for k in range(MAP_SIZE):
        print(MAP[j][k],end=" ")
    print()