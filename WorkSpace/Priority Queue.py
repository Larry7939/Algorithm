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
        if self.isEmpty():
            return None
        else:
            highest =0
            for i in range(1,self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.item[highest]
q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)
print("PQueue:",q.items)
while not q.isEmpty():
    print("Max Priority: ",q.dequeue())

