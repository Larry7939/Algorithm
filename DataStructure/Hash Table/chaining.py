class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
class ChainHash:
    def __init__(self,capacity:int) -> None:
        self.capacity = capacity
        self.table = [None]*capacity
    def hash_value(self,key)->int:
        return key%self.capacity


    def search(self,key):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if(p.key == key):
                return p.value
            p = p.next
        return None
    def insert(self,key,value)->bool:
        #동일한 키가 존재하는 지 끝 노드까지 검사한 후에, 없으면 체인 맨 앞에 추가
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return False
            p = p.next
        temp = Node(key,value,self.table[hash])
        self.table[hash] = temp
        return True
    def remove(self,key)->bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None #직전 노드 pp
        while p is not None:
            if p.key == key:
                #pp가 None, 즉 p가 해당 연결리스트의 첫 노드인 상황
                if pp is None:
                    self.table[hash] = p.next
                #직전 Node가 존재하는 상황. 직전 노드와 현재 노드의 다음 노드를 이어버리면 삭제 가능
                else:
                    pp.next = p.next
                return True
            #현재 노드가 직전노드(pp)가 됨
            pp = p 
            #다음 노드 주목
            p = p.next
        return False
    #해시테이블을 덤프
    #각 노드의 키와 값을 출력한다.
    def dump(self)->None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i,end='')
            while p is not None:
                print(f' ->{p.key}({p.value})',end='')
                p = p.next
            print()
    def __getitem__(self,key):
        return self.search(key)
    def __setitem__(self,key,value):
        return self.insert(key,value)
        
ch = ChainHash(5)
ch.insert(15,'김')
ch.insert(45,'박')
ch.insert(13,'이')
ch.insert(34,'최')
ch.insert(51,'오')
ch.insert(28,'정')
ch.insert(43,'주')
ch.insert(16,'성')
ch.dump()
print(ch[15])
print(ch[34])
