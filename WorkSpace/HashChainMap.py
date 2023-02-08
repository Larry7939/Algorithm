class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s:%s"%(self.key,self.value))
class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
class HashChainMap:
    def __init__(self,M):
        self.table = [None]*M
        self.M = M
    def hashFn(self,key):
        sum = 0
        for c in key:
            sum = sum+ord(c)
        return sum%self.M
    def insert(self,key,value):
        idx = self.hashFn(key)
        self.table[idx] = Node(Entry(key,value),self.table[idx])
        #위 한줄이랑 아래 네줄이랑 같은 말 아닌가? 이거 주석처리하고 실행해보자. # 같은 거 맞음~
        # entry = Entry(key,value)
        # node = Node(entry)
        # node.link = self.table[idx]
        # self.table[idx] = node
    def search(self,key):
        idx = self.hashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node = node.link
        return None
    def delete(self,key):
        idx = self.hashFn(key)
        before = self.table[idx]
        node = before.link
        if before.data.key == key and before.link is None: self.table[idx]=None #딱 하나밖에 없었다면, 그걸 None으로 만든다.
        elif before.data.key == key and before.link is not None: self.table[idx]=before.link #맨 처음인데, 그 뒤에 node가 있으면, 그 node를 table에 넣는다. 
        else: #두번째 node부터는 before와 node를 둘 다 link를 타고 가다가 key가 같으면 before.link와 해당 node의 link를 연결해준다.
            while node is not None:
                if node.data.key == key:
                    before.link = node.link
                before = before.link
                node = node.link
    def display(self,msg):
        print("나의 단어장: ")
        for i in range(self.M):
            if self.table[i] is not None:
                print("[%d]"%i,end=' -> ')
                node = self.table[i]
                while node is not None:
                    print(node.data,end=' -> ')
                    node = node.link
                print()
map = HashChainMap(13)
map.insert('data','자료')
map.insert('structure','구조')
map.insert('sequential search','선형탐색')
map.insert('game','게임')
map.insert('binary search','이진탐색')
map.display('나의 단어장: ')
print("탐색:game -->",map.search('game'))
print("탐색:over -->",map.search('over'))
print("탐색:data -->",map.search('data'))
map.delete('game')
map.display('나의 단어장: ')
