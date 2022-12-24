from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(list(stack))
stack.pop()
stack.pop()
stack.pop()
print(*stack)