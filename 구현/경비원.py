#BOJ 2564 경비원
import sys
#입력값


# 북쪽(1), 남쪽(2), 서쪽(3), 동쪽(4)
# 상점의 위치(위치,경계로부터의 거리)
# 북쪽(1), 남쪽(2)에 위치한 경우, 블록의 왼쪽 경계로부터의 거리
# 서쪽(3), 동쪽(4)에 위치한 경우, 블록의 위쪽 경계로부터의 거리
#모든 위치는 블록의 꼭짓점이 될 수 없다.
# 매번 다른 방향으로 돌아볼 필요 없이, 시계방향으로만 돌면서
# 블록 둘레의 길이를 길이로 하는 1차원 배열로 만들어서, 여기에 상점을 배치하면 된다.(북쪽이 시작 경계)
# start(동근)으로부터 오른쪽 왼쪽에 있는 상점을 찾아내서 인덱스를 뺀 다음 비교해서 최솟값만을 result에 더하면 된다.
def getRightDistance(w,distance): #오른쪽 거리를 구해주는 함수
    return abs(w-distance)
def getBottomDistance(h,distance): #아래쪽 거리를 구해주는 함수
    return abs(h-distance)
def setBlock(block,w,h,direction,distance,indicator):
    if direction == 1: #북쪽
        block[distance] = indicator
    elif direction == 2: #남쪽
        block[block_height+block_width+getRightDistance(w,distance)] = indicator
    elif direction == 3: #서쪽
        block[block_height+2*block_width+getBottomDistance(h,distance)] = indicator
    elif direction == 4: #동쪽
        block[getRightDistance(w,distance)+distance] = indicator
def getMinDistance(count,block_round):
    return min(count, block_round-count)

directions = [1,4,2,3]
# 블록의 크기(가로,세로)
block_width,block_height = map(int,sys.stdin.readline().split()) 
# 상점의 개수
n = int(sys.stdin.readline()) 
# 블록의 둘레
block_round = 2*(block_width+block_height)
block = [0]*block_round
for _ in range(n):
    direction,distance = map(int,sys.stdin.readline().split())
    setBlock(block,block_width,block_height,direction,distance,1)
start_direction,start_distance = map(int,sys.stdin.readline().split()) #동근이의 위치
setBlock(block,block_width,block_height,start_direction,start_distance,2)

start_index = block.index(2)

result = 0 #총 최소 거리
cnt = 0
for i in range(1,block_round):
    cnt += 1
    i = (start_index+i) % block_round
    if block[i] == 1:
        block[i] = 0
        result += getMinDistance(cnt,block_round)

print(result)
