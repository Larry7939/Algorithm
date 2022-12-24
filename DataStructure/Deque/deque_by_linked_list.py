class Deque_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class Deque:
    def __init__(self):
        self.front = Deque_Node('dummy')
        self.rear = Deque_Node('dummy')
        self.front.next, self.rear.prev = self.rear, self.front
        self.size = 0

    def is_empty(self):
        return self.size == 0

    #front와 rear는 더미노드로 고정
    #더미노드(front) - 데이터 노드 - 더미노드(rear)
    #이런 형태를 취한 상태에서 추가 및 삭제 수행
    def append_left(self, data) -> None:
        new_node = Deque_Node(data, self.front, self.front.next)
        new_node.next.prev = new_node
        self.front.next = new_node
        self.size += 1

    def append(self, data) -> None:
        new_node = Deque_Node(data, self.rear.prev, self.rear)
        new_node.prev.next = new_node
        self.rear.prev = new_node
        self.size += 1

    def pop_left(self):
        if self.is_empty():
            return
        removed = self.front.next
        removed_data = removed.data
        self.front.next = removed.next
        removed.prev = self.front
        self.size -= 1
        return removed_data

    def pop(self):
        if self.is_empty():
            return
        removed = self.rear.prev
        removed_data = removed.data
        self.rear.prev = removed.prev
        removed.prev.next = self.rear
        self.size -= 1
        return removed_data

    def peek_front(self):
        if self.is_empty():
            return
        return self.front.next.data
    def peek_rear(self):
        if self.is_empty():
            return
        return self.rear.prev.data
    def size(self):
        return self.size
    
    def __iter__(self):
        node = self.front.next
        while node != self.rear:
            #return 키워드를 사용할 때에는 결과값을 딱 한번만 제공
            #yiedl 키워드를 사용할 때에는 결과값을 여러 번 나누어서 제공
            #리스트를 반환하는 대신 generator객체를 반환하여 
            #필요할 때마다 즉석에서 하나씩 만들어낼 수 있도록 한다.
            #메모리에 한번에 올리기 부담스러운 스트림 데이터를 처리할 때, yield가 메모리 효율 측면에서 효율적이다.
            yield node 
            node = node.next
    def __str__(self) -> str:
        return '->'.join(str(node) for node in self)
dq = Deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append_left(3)
dq.append_left(2)
dq.append_left(1)
print(dq)
print(dq.size)
dq.pop_left()
dq.pop()
print(dq)
print(dq.size)

