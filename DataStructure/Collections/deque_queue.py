from collections import deque

my_queue = deque(maxlen=10)
for i in range(10):
    my_queue.append(i+1)
print(my_queue)
# >>> deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], maxlen=10)

my_queue.append(11)
print(my_queue)
# >>> deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], maxlen=10)
# 처음에 1부터 10까지의 값이 들어가도록 했다. 최대 길이를 10으로 설정했으므로, 11이 들어갈 때에는 가장 앞에 있던 값인 1이 빠져 나오게 되는 queue 자료구조이다.