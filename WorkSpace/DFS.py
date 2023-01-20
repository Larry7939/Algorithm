class Stack():
    def __init__(self):
        self.top=[]
    def isEmpty(self): return len(self.top)==0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def size(self): return len(self.top)
    def clear(self): self.top=[]
    def __str__(self):
        return str(self.top[::-1])

#깊이우선 탐색(Depth First Search)
map = [['1','1','1','1','1','1'],
       ['e','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','1','1','0','0','x'],
       ['1','1','1','0','1','1'],
       ['1','1','1','1','1','1']
      ]
MAZE_SIZE = 6
#x랑 y랑 뒤바뀜.
#map[y][x]임.
#map[1] = ['e','0','0','0','0','1']
#map [1,0] = e

def isValidPos(x,y):
    #여기에서 x>MAZE_SIZE or y>MAZE_SIZE에서 >=가 아닌 이유는,
    #미로를 만들때 교수님이 테두리에 전부 벽을 쳐서 그런거임.
    #벽부분에 길이 있으면 list out of range 오류 뜸.
    if x<0 or y<0 or x>MAZE_SIZE or y>MAZE_SIZE:
        return False
    else:
        #0(비어있음) 이거나 x(목적지)면 True반환. 나머지는 전부 False
        return map[y][x] == '0' or map[y][x] =='x'

def DFS():
    stack = Stack()
    #맨 처음 시작위치
    stack.push((0,1))
    print('DFS: ')
    #스택이 비면 더이상 갈 곳이 없어서 끝나는 거임.
    while not stack.isEmpty():
        #처음 시작지점을 갔을 때, 그 지점이 pop()되는 것이다.
        here = stack.pop()
        print(here,end='->')
        (x,y) = here
        if(map[y][x]=='x'): return True
        else:
            #지나온 점을 표시
            map[y][x] = '.'
            #4방향의 output을 검사해서 갈 수 있으면, 스택에 삽입한다.
            #y-1은 위쪽으로 가는 것을 위미한다. 즉, 위쪽을 제일 먼저 확인해서 스택에 집어넣는다.
            #우선순위에 따라, 나중에 map을 출력했을 때, .의 위치가 조금씩 다르다.
            #상
            if isValidPos(x,y-1): stack.push((x,y-1))
            #하
            if isValidPos(x,y+1): stack.push((x,y+1))
            #좌
            if isValidPos(x-1,y): stack.push((x-1,y))
            #우
            if isValidPos(x+1,y): stack.push((x+1,y))
            #코딩테스트에 이런 문제 나오니까 잘 봐라.
        print("현재 스택: ",stack)
        #우측부터 먼저 간다.왜냐면, pop하면서 가는 것이기 때문에, 맨 마지막에 push하는 곳으로 먼저 가는 것이다!
        #우,좌,하,상의 순서로 간다.
    #다 끝났는데도 x를 못만나면 return False
    return False
result = DFS()
if result: print("-->미로탐색 성공")
else: print("-->미로탐색 실패")
for i in map:
    print(i)
