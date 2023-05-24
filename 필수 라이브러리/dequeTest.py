from collections import deque

a = [1,2,3,4]
a = deque(a)
a.append(1)
a.appendleft(-1)
print(list(a))

