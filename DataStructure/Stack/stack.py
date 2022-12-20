class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self) -> bool:
        return len(self.stack)

    def __str__(self):
        return str(self.stack[::-1])

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop(-1)
        else:
            print("stack underflow")
            exit()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("underflow")
            exit()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
print(s)
