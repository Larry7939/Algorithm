class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s:%s"%(self.key,self.value))
def sequential_search(A,key,low,high):
    for i in range(low,high+1):
        if A[i].key==key:return i
    return None
class SequentialMap:
    def __init__(self):
        self.table=[]
    def insert(self,key,value):
        self.table.append(Entry(key,value))
    def size(self):
        return len(self.table)
    def search(self,key):
        pos = sequential_search(self.table,key,0,self.size()-1)
        if pos is not None: return self.table[pos]
        else: return None
    def delete(self,key):
        for i in range(self.size()):
            if self.table[i].key ==key:
                self.table.pop(i)
                return
    def display(self,msg):
        print("나의 단어장: ")
        for i in range(self.size()):
            print("  ",self.table[i])
map = SequentialMap()
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
map.display("나의 단어장: ")