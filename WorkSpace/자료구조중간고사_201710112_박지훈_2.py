class Node:
    def __init__(self,elem,link=None):
        self.data = elem
        self.link =link
class LinkedList:
    def __init__(self):
        self.head =None
    def isEmpty(self):
        return self.head ==None
    def clear(self):
        self.head =None
    def size(self):
        count=0
        node = self.head
        while not node == None:
            node = node.link
            count+=1
        return count
    def display(self,msg="Linked List: "):
        print(msg,end='')
        node =self.head
        while not node==None:
            print(node.data,end=' ')
            node = node.link
        print()
    def getNode(self,pos):
        if pos<0: return None
        node = self.head
        while pos>0 and node!=None:
            node = node.link
            pos -=1
        return node
    def getEntry(self,pos):
        node = self.getNode(pos)
        if node ==None: return None
        else: return node.data
    def replace(self,pos,elem):
        if not self.getNode(pos)==None:
            self.getNode(pos).data = elem
    def find(self,val):
        node = self.head
        while node is not None:
            if node.data ==val: return node
            node = node.link
    def insert(self,pos,elem):
        before = self.getNode(pos-1)
        if before ==None:
            self.head = Node(elem,self.head)
        else:
            node = Node(elem,before.link)
            before.link = node
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before ==None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link!=None:
            before.link = before.link.link
def concatList(LinkedList1,LinkedList2):
    MergedList = LinkedList()
    size1=LinkedList1.size()
    size2=LinkedList2.size()
    for i in range(size1):
        MergedList.insert(i,LinkedList1.getEntry(i))
    for i in range(size2):
        MergedList.insert(i+size1,LinkedList2.getEntry(i))
    MergedList.display('MergedList: ')
LinkedList1 = LinkedList()
LinkedList2 = LinkedList()
LinkedList1.insert(0,'a')
LinkedList1.insert(1,'b')
LinkedList1.insert(2,'c')
LinkedList2.insert(0,'x')
LinkedList2.insert(1,'y')
LinkedList2.insert(2,'z')
LinkedList1.display()
LinkedList2.display()
concatList(LinkedList1, LinkedList2)
