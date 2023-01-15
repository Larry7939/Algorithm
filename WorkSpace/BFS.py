MAX_QSIZE=10
class CircularQueue:
    def __init__(self):
        self.front =0
        self.rear =0
        self.items = [None]*MAX_QSIZE
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front ==(self.rear+1)%MAX_QSIZE
    def clear(self):
        self.front = self.rear
    def enqueue(self,item):
        if not self.isFull():
            self.rear=(self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        #self.rear가 front보다 작을 수도 있으니, MAX_QSIZE를 더해놓고, front로 뺀다.
        return (self.rear+MAX_QSIZE-self.front)%MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE]\
                +self.items[0:self.rear+1]
        print("[f=%d,r=%d]==>"%(self.front,self.rear),out)
MAZE_SIZE = 6
def isValidPos(x,y):
    if x>MAZE_SIZE or y>MAZE_SIZE or x<0 or y<0:
        return False
    else:
        if map[y][x] =='0' or map[y][x] =='x':
            return True
def BFS():
    que = CircularQueue()
    que.enqueue((0,1))
    print("BFS: ")
    while not que.isEmpty():
        here = que.dequeue()
        print(here,end="->")
        x,y=here
        if(map[y][x] =='x'):return True
        else:
            map[y][x]='.'
            if isValidPos(x,y-1):que.enqueue((x,y-1))
            if isValidPos(x,y+1):que.enqueue((x,y+1))
            if isValidPos(x-1,y):que.enqueue((x-1,y))
            if isValidPos(x+1,y):que.enqueue((x+1,y))
    return False
map = [['1','1','1','1','1','1'],
       ['0','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']]
result = BFS()
if result: print("-->미로탐색 성공")
else: print("-->미로탐색 실패")
for i in map:
    print(i)