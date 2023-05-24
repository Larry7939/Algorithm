import heapq
q = []

heapq.heappush(q,2)
heapq.heappush(q,4)
heapq.heappush(q,1)
print(q)
print(heapq.heappop(q))
print(q)
print(heapq.heappop(q))
print(q)
print(heapq.heappop(q))
print(q)