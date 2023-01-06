from collections import deque
stack = deque()
for i in range(10):
    stack.append(i+1)
# .pop() 메소드를 사용하면 가장 뒤에 있는 값인 10 이 빠져나오는는 stack 구조이다.
stack.pop()
print(stack)
# stack.pop()을 출력하면 꺼낸 element가 나오고, 이 element를 stack에서 꺼낸 것이므로 stack을 다시 출력하면 element가 제외된다.
print(stack.pop())
print(stack)