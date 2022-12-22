# Linked List
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        count = 0
        node = self.head
        while (node != None):
            node = node.link
            count += 1
        return count

    def display(self,msg="Linked List"):
        print(msg,end=' ')
        node = self.head
        while (node != None):
            print(node.data, end=' => ')
            node = node.link
        print()

    def getNode(self, pos):  # pos번째 노드 반환
        if pos < 0:
            return None
        node = self.head
        #pos가 0이면, while문에 안들어가고 그냥 끝나면 된다.
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        #pos가 1이면 1번째 node를 꺼낸다.
        #2이면 link를 두번 타고가서 2번째 node를 꺼낸다.
        return node

    def getEntry(self, pos):  # pos번째 노드 data 반환
        #노드가 반환된다. 그냥 None인지만 검사하고 node.data를 반환한다.
        node = self.getNode(pos) 
        if (node == None):
            return None
        else:
            return node.data

    def replace(self, pos, elem):
        if self.getNode(pos) != None:
            self.getNode(pos).data = elem

    def find(self, elem):
        node = self.head #elem를 가지고있는 node를 출력한다.
        while(node != None):
            if node.data == elem:#돌아가면서 val을 data로 갖는 node를 찾는다.
                return node
            node = node.link
#사실 이게 중요한 게 아니다. insert와 delete하기 위해 필요한 
# getNode를 구현하기 위한 과정이였을 뿐이다.
    def insert(self,pos,elem):
        before = self.getNode(pos-1) #pos의 바로 전 노드
        if before == None: #맨 앞에 삽입하는 경우
            self.head = Node(elem,self.head) #그 다음 링크는 현재 head를 가리키게 한다. 아마 None
        else:
            #뭔가가 있는 경우, 즉, before가 None이 아닌경우
            #before의 next를 Node의 next로 주고,
            node = Node(elem,before.link)
            #before의 next에 새로 만들어진 node가 들어간다.
            before.link = node
    def delete(self,pos):
        #삭제하고 싶은 것이 있으면, before의 next가 pos의 next되게끔 한다.
        before = self.getNode(pos-1)
        #시작 노드를 삭제하는 상황
        if before==None:
            #self.head가 None이면, 이것도 해줄 필요 없다.
            if self.head != None:
                self.head = self.head.link
        elif before.link!=None:
            #before.link는 현재의 나, 그 다음 next랑 연결해준다.
            before.link = before.link.link

l = LinkedList()
l.insert(0,10);l.insert(1,20);l.insert(2,30)
l.display()
l.replace(1,50)
l.display()
l.delete(l.size()-1)
l.display()
l.clear()
l.display()