#Linked Stack
class Node:
    #데이터 elem과, link(초기값은 None)
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link
class LinkedStack:
    def __init__(self):
        #헤드 포인터는 None
        self.top=None
    def isEmpty(self): return self.top==None
    def clear(self): self.top =None
    #헤드 포인터는 맨 앞에 놓으므로, 
    #데이터가 삽입되면 top이 새로 들어오는 데이터를 가리키면 된다.
    #새로 들어오는 데이터가 원래 top이 가리키던 녀석을 가리키면 된다.
    def push(self,item):
        #새로 들어온 데이터로 노드를 만들고, 원래 top이 가리키던 녀석을 가리키게 만든다.
        n = Node(item,self.top)
        #self.top이 n을 가리키게 한다.
        self.top = n
    def pop(self):
        if not self.isEmpty():
            #지금 top이 가리키는 노드를 변수 n에 넣고,
            #top은 n의 다음 노드를 가리키게 한다.
            #n은 return
            n = self.top
            self.top = n.link
            return n.data
    def size(self):
        #끝까지 count
        node = self.top
        count=0
        while not node == None:
            node = node.link
            count+=1
        return count
    def display(self,msg='LinkedStack'):
        print(msg,end=' ')
        node = self.top
        while not node ==None:
            print(node.data,end=' ')
            node = node.link
        print()
#LinkedStructure가 좀 더 복잡하기 때문에, 여러번 연습해봐야한다.
#결국은 배열로 구현하냐, 이걸로 구현하냐인데, 큐,덱으로 가면 더 복잡해진다. 이중구조도 하려면..
#복잡해질 수록 시간 복잡도는 줄어들지만, 코드는 복잡해진다. 
# 그래서 일반적인 프로그래밍을 할 때는 배열을 사용하는 게 좀 더 간단하게 구현할 수 있다.
odd = LinkedStack()
even = LinkedStack()
for i in range(10):
    if i%2==0: even.push(i)
    else: odd.push(i)
odd.display()
even.display()
odd.pop()
odd.pop()
odd.display()
odd.push(11)
odd.display()
print("SIZE: ",odd.size())
