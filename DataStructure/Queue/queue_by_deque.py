from collections import deque

# (reverse를 하지 않은 기준으로)
# 오른쪽에서 왼쪽으로 향하는 터널을 생각하면 연상이 쉽다.
# 단순 리스트로 큐를 구현하게 되면,
# pop() 메서드에 index를 입력하고,
# 해당 인덱스 값을 반환한 후 조정하는 과정에서
# O(k)의 시간복잡도가 발생하므로,
# 큐는 deque 모듈을 사용하는 것이 좋다.
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
print(queue)
queue.reverse()
print(queue)
