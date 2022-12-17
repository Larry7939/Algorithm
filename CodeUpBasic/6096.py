def showStatus():
    for i in range(MAP_SIZE):
        print(*MAP[i])
def convertMarker(x:int):
    if(x==0):
        return 1
    else:
        return 0
MAP_SIZE = 19
MAP = [[0]*MAP_SIZE for _ in range(MAP_SIZE)]

for i in range(MAP_SIZE):
    MAP[i] = list(map(int,input().split()))
n = int(input()) #십자 뒤집기 횟수
for j in range(n):
    (y,x) = list(map(int,input().split()))
    for k in range(MAP_SIZE): #행 뒤집기
        MAP[y-1][k] = convertMarker(MAP[y-1][k])
    for p in range(MAP_SIZE): #열 뒤집기
        MAP[p][x-1] = convertMarker(MAP[p][x-1])
showStatus()

