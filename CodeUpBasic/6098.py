def showStatus(h: int):
    for i in range(h):
        print(*MAP[i])


MAP_SIZE = 10
MAP = [[0]*MAP_SIZE for _ in range(MAP_SIZE)]

for i in range(MAP_SIZE):
    MAP[i] = list(map(int, input().split()))
currentX = 1
currentY = 1
MAP[currentY][currentX] = 9
while (True):
    if (MAP[currentY][currentX+1] == 0):
        MAP[currentY][currentX] = 9
        currentX += 1
    elif (MAP[currentY+1][currentX] == 0):
            MAP[currentY][currentX] = 9
            currentY += 1
    elif (MAP[currentY+1][currentX] == 1 and MAP[currentY][currentX+1] == 1 ):
        MAP[currentY][currentX] = 9
        break
    else:
        if (MAP[currentY][currentX+1] == 2):
            MAP[currentY][currentX] = MAP[currentY][currentX+1] = 9
            break
        elif (MAP[currentY+1][currentX] == 2):
            MAP[currentY][currentX] = MAP[currentY+1][currentX] = 9
            break
showStatus(MAP_SIZE)
