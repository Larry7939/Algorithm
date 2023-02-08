from typing import Any
class FixedStack:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    def __init__(self,capacity:int=256)->None:
        self.stk = [None]*capacity
        self.capacity = capacity
        self.ptr = 0 #스택 포인터는 0
    def __len__(self)->int:
        return self.ptr
    def is_empty(self)->bool:
        return self.ptr<=0
    def is_full(self)->bool:
        return self.ptr>=self.capacity
    #스택에 데이터를 추가하고, 가득 찬 경우엔, 예외처리 Full을 이용한다.
    #스택의 꼭대기에서 데이터를 꺼내서 그 값을 반환한다. 비어있는 경우에는 Empty를 통해 예외처리를 내보낸다.
    #peek()함수는 꼭대기 데이터를 들여다본다. 비어있는 경우에는 Empty를 통해 예외처리를 내보낸다.
    #비어있지 않으면, 꼭대기 원소 stk[ptr-1]를 반환한다. 데이터 입출력이 아니므로, 스택포인터의 변화는 없다.
    def push(self,value:Any)->None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr+=1
    def pop(self) ->Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr-=1
        return self.stk[self.ptr]
    def peek(self) ->Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    #모든 데이터 삭제
    def clear(self)->None:
        self.ptr=0
    def find(self,value:Any)->Any:
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i] ==value:
                return i
        return -1
    def count(self,value:Any)->bool:
        c=0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c+=1
        return c
    #스택에 value가 있는지 판단
    #클래스에 위의 __len__함수를 정의하면, x.len(), len(x) 이 두가지 방식으로 사용할 수 있다.
    #마찬가지로 stk.__contains__(x)를  x in stk로 간단히 작성할 수 있다.
    #contains(x) 이렇게 쓸 수도 있다!
    #이런 식으로 언더바가 2개인 함수를 던더함수라고 한다.
    def __contains__(self,value:Any)->bool:
        return self.count(value)

    def dump(self)->None:
        if self.is_empty():
            print("스택이 비어있습니다.")
        else:
            print(self.stk[:self.ptr])
