from typing import Any
from collections import deque
class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    def __init__(self,capacity:int)->None:
        self.front =0
        self.rear=0
        self.no=0
        self.capacity = capacity
        self.que = [None]*capacity
    def __len__(self)->int:
        return self.no
    def is_empty(self)->bool:
        return self.no<=0
    def is_full(self)->bool:
        return self.no>=self.capacity
    def enqueue(self,x:Any)->None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear +=1
        self.no+=1
        if self.rear ==self.capacity:
            self.rear=0
    def dequeue(self)->Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front+=1
        self.no-=1
        if self.front==self.capacity:
            self.front =0
        return x
    def peek(self)->Any:
        if self.is_empty():
            raise FixedQueue.Empty
        #들여다 보는 것 뿐이기 때문에, front는 변경시키지 않는다.
        return self.que[self.front]
    def find(self,value:Any)->Any:
        for i in range(self.no):
            #큐에서의 스캔은 배열의 맨 앞부터가 아니라,
            #큐의 맨 앞 원소에서부터 시작한다.
            #따라서, self.front를 1씩 증가시키면서, self.capacity를 넘어가면
            #0으로 돌아가게끔 나머지 연산을 한다.
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    def count(self,value:Any)->bool:
        c=0
        for i in range(self.no):
            #여기에서도 마찬가지로 큐의 맨 앞 원소의 인덱스 front부터
            #1증가씩 증가시키면서 c를 +1한다.
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value:
                c+=1
        return c
    def __contains__(self,value:Any)->bool:
        return self.count(value)
    def clear(self)->None:
        self.no=self.front=self.rear=0
    def dump(self)->None:
        if self.is_empty():
            print("큐가 비었습니다.")
        else:
            for i in range(self.no):
                idx = (i+self.front)%self.capacity
                print(self.que[idx],end=' ')
            print()



