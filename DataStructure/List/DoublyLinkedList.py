class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None,self.head)
        self.head.next = self.tail
        self.size = 0
    def listSize(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def selecNode(self,idx):
        if idx>self.size:
            print("Overflow : index error")
        if idx == 0:
            return self.head
        if idx ==self.size:
            return self.tail
        if idx <= self.size//2:
            target = self.head
            for _ in range(idx):
                target = target.next
                return target
        else:
            target = self.tail
            for _ in range(idx):
                target = target.prev
                return target
    def appendLeft(self,value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = Node(None,self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(value,None,tmp)
            tmp.prev = self.head
        self.size+=1
    def append(self,value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = Node(None,self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(value,tmp,self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size+=1
    def insert(self,value,idx):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = Node(None,self.head)
            self.head.next = self.tail
        else:
            tmp = self.selecNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendLeft(value)
            elif tmp == self.tail:
                self.append(value)
            else:
                tmp_prev = tmp.prev
                newNode = Node(value,tmp_prev,tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
            self.size += 1
    def delete(self,idx):
        if self.isEmpty():
            print("UnderFlow Error")
            return
        else:
            tmp = self.selecNode(idx)
            if tmp==None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
            else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del(tmp)
            self.size -=1
    def printList(self):
        target = self.head
        while target != self.tail:
            if target.next != self.tail:
                print(target.data,'<=> ',end='')
            else:
                print(target.data)
            target = target.next
    
mylist = DList()
mylist.append('A')
mylist.printList()
mylist.append('B')
mylist.printList()
mylist.append('C')
mylist.printList()
mylist.insert('D', 1)
mylist.printList()
mylist.appendLeft('E')
mylist.printList()
print(mylist.listSize())
mylist.delete(0)
mylist.printList()
mylist.delete(3)
mylist.printList()
mylist.delete(0)
mylist.printList()
mylist.appendLeft('A')
mylist.printList()


        

