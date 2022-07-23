#큐
Q_Size = 10
class Queue():
    def __init__(self):
        self.items = [0]*Q_Size
        self.s=0
    def empty(self):
        if self.s ==0:
            return True
        else:
            return False
    def push(self, x):
        self.items[self.s] = x
        self.s+=1
    def pop(self):
        if not self.empty():
            self.s-=1
            return self.items.pop(0)
        else:
            return -1
    def size(self):
        return self.s
    def front(self):
        if not self.empty():
            return self.items[0]
        else:
            return -1
    def back(self):
        if not self.empty():
            return self.items[self.s-1]
        else:
            return -1
q = Queue()
t = int(input())
for _ in range(t):
    qe = input().split()
    if qe[0] == "push":
        q.push(qe[1])
    elif qe[0] == "pop":
        if q.empty() : 
            print(-1)
        else:
            print(q.pop())
    elif qe[0] == "size":
        print(q.s)
    elif qe[0] == "empty":
        if q.empty() : 
            print(1)
        else:
            print(0)
    elif qe[0] == "front":
        if q.empty(): 
            print(-1)
        else:
            print(q.front())
    elif qe[0] == "back":
        if q.empty() :
            print(-1)
        else:
            print(q.back())

