MAX_QSIZE = 10
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
        return (self.rear+MAX_QSIZE-self.front)%MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE]\
                +self.items[0:self.rear+1]
        print("[f=%d,r=%d]==>"%(self.front,self.rear),out)

class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self,item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self,item):
        if not self.isFull():
            self.items[self.front]=item
            self.front=(self.front-1)%MAX_QSIZE
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear-1)%MAX_QSIZE
            return item
    def getRear(self):
        return self.items[self.rear]
