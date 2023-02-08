class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top)==0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        return self.top.pop(-1)
    def peek(self):
        return self.top[-1]
    def size(self):
        return len(self.top)
    def clear(self):
        self.top = []
    def __str__(self):
        return str(self.top[::-1])
stack =Stack()
string = input("문자열을 입력하세요.")
for s in string:
    stack.push(s)
for i in range(stack.size()):
    print(stack.pop(),end='')