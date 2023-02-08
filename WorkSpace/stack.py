from collections import deque
from typing import Any
class Stack:
    def __init__(self,maxlen:Any=256)->None:
        self.capacity = maxlen
        self.__stk=deque([],maxlen)
    def __len__(self)->int:
        return len(self.__stk)
    def is_empty(self)->bool:
        return not self.__stk
    def if_full(self)->bool:
        return len(self.__stk)==self.__stk.maxlen #self.capacity가 더 맞지 않나?
    def push(self,value:Any):
        self.__stk.append(value)
    def pop(self)->Any:
        return self.__stk.pop()
    def peek(self) ->Any:
        return self.__stk[-1]
    def clear(self)->None:
        self.__stk.clear()
    def find(self,value:Any)->Any:
        try:
            #스택에서 value를 찾아 인덱스 반환
            return self.__stk.index(value)
        except ValueError:
            return -1
    def count(self,value:Any)->int:
        #스택에 포함되어있는 value 개수 반환
        return self.__stk.count(value)
    def __contains__(self,value:Any)->bool:
        return self.count(value)
    def dump(self)->int:
        print(list(self.__stk))