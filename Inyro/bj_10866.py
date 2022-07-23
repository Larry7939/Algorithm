Deque_Size = 100
class Deque():
    def __init__(self):
        self.s = 0
        self.items = [None]*Deque_Size
    def push_front(self,x):
        self.items.insert(0,x)
        self.s+=1
    def push_back(self,x):
        self.items.append(x)
        self.s+=1
    def pop_front(self):
        if(self.s==0):
            return -1
        else:
            self.s -= 1
            return self.items.pop(0)

    def pop_back(self):
        if(self.s==0):
            return -1
        else:
            self.s -= 1
            return self.items.pop(-1)
    def size(self):
        return self.s
    def empty(self):
        if(self.s==0):
            return 1
        else:
            return 0
    def front(self):
        if(self.empty()==1):
            return -1
        else:
            return self.items[0]
    def back(self):
        if(self.empty()==1):
            return -1
        else:
            return self.items[-1]
dq = Deque()
t = int(input())
for _ in range(t):
    qe = input().split()
    if qe[0] == "push_front":
        dq.push_front(qe[1])
    elif qe[0] == "push_back":
        dq.push_back(qe[1])
    elif qe[0] == "pop_front":
        print(dq.pop_front())
    elif qe[0] == "pop_back":
        print(dq.pop_back())
    elif qe[0] == "size":
        print(dq.size())
    elif qe[0] == "empty":
        print(dq.empty())
    elif qe[0] == "front":
        print(dq.front())
    elif qe[0] == "back":
        print(dq.back())

