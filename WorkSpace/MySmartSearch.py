import math
class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        #우선순위가 가장 높은 것을 뺀다.
        #가장 값이 큰 것을 뺀다.
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def findMaxIndex(self):
        #값이 가장 큰 원소의 인덱스를 반환하는 함수
        if self.isEmpty(): return None
        else:
            highest =0
            for i in range(1,self.size()):
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
            return highest
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.item[highest]
(ox,oy) = (5,4) #목적지 좌표
def dist(x,y):
    (dx,dy)=(ox-x,oy-y)
    return math.sqrt(dx*dx+dy*dy)
MAZE_SIZE = 6
def isValidPos(x,y):
    if x>MAZE_SIZE or y>MAZE_SIZE or x<0 or y<0:
        return False
    else:
        if map[y][x] =='0' or map[y][x] =='x':
            return True
def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1))) #거리정보를 추가한 튜플 enqueue
    print("PQueue: ")
    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2],end='->')
        x,y,_=here
        if(map[y][x]=='x'):return True
        else:
            map[y][x]='.'
            if isValidPos(x,y-1): q.enqueue((x,y-1,-dist(x,y-1)))
            if isValidPos(x,y+1): q.enqueue((x,y+1,-dist(x,y+1)))
            if isValidPos(x-1,y): q.enqueue((x-1,y,-dist(x-1,y)))
            if isValidPos(x+1,y): q.enqueue((x+1,y,-dist(x+1,y)))
        print("우선순위큐:",q.items)
    return False
map = [['1','1','1','1','1','1'],
       ['0','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']]
result = MySmartSearch()
if result: print("-->미로탐색 성공")
else: print("-->미로탐색 실패")
for i in map:
    print(i)