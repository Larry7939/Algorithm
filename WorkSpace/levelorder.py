MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.rear =0
        self.front =0
        self.items =[None]*MAX_QSIZE
    def isEmpty(self):
        return self.rear==self.front
    def isFull(self):
        return (self.rear+1)%MAX_QSIZE == self.front
    def clear(self):
        self.front = self.rear
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear+MAX_QSIZE-self.front)%MAX_QSIZE
    def display(self):
        out =[]
        if self.front < self.rear:
           out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%d,r=%d]==>"%(self.front,self.rear),out)
class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None: #만약 자식노드가 있다면,
            print(n.data,end=' ') #꺼내서 출력하고, 자식노드들을 큐에 집어넣는다.(그림참고)
            queue.enqueue(n.left)
            queue.enqueue(n.right)
#그림과 같은 트리를 만들어준다.
d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',f,None)
root = TNode('A',b,c)
print("Level-Order")
levelorder(root)
