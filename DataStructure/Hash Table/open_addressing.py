class OpenHash:
    def __init__(self, n: int):
        self.capacity = n
        self.table = [None] * self.capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def hash_value(self, i, key) -> int:
        return (key+i) % self.capacity #i를 더해서 재해시

    def search(self, key):
        for i in range(self.capacity):
            hash = self.hash_value(key, i) #i를 더해서 재해시
            if self.table[hash] is None:
                return
            elif self.table[hash] != None and self.table[hash][0] == key:
                return self.table[hash][1]

    def insert(self, key, value) -> None:
        if self.is_full():
            return
        for i in range(self.capacity):
            hash = self.hash_value(key, i) #i를 더해서 재해시
            # self.table[hash]가 비어있거나 삭제된 경우에는 insert
            if self.table[hash] is None or self.table[hash] == None:
                self.table[hash] = [key, value]
                return
            # key가 동일한 경우에는 value 업데이트
            if self.table[hash][0] == key:
                self.table[hash][1] = value
                return

    def delete(self, key) -> None:
        for i in range(self.capacity):
            hash = self.hash_value(key, i) #i를 더해서 재해시
            if self.table[hash] is None:
                return
            elif self.table[hash] != None and self.table[hash][0] == key:
                self.table[hash] = None
                self.size -= 1
                return
    def __getitem__(self,key):
        return self.search(key)
    def __setitem__(self,key,value):
        return self.insert(key,value)

oh = OpenHash(5)
oh[0] = '김'
oh[1] = '박'
oh[2] = '최'
oh[3] = '황'
oh[4] = '오'
print(oh[1])
print(oh[2])
print(oh[4])
oh.delete(2)
print(oh[1])
print(oh[2])
print(oh[4])