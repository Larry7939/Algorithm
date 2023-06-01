import heapq
# 무지의 먹방 라이브
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []

    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    now_food = 0
    before_food = 0
    all_food_count = len(food_times)
    cur_sum = 0
    while cur_sum + (q[0][0] - before_food) * all_food_count <= k:
        now_food = heapq.heappop(q)
        cur_sum += (now_food[0] - before_food) * all_food_count
        all_food_count -= 1
        before_food = now_food[0]
    
    result = sorted(q,key=lambda x: x[1])
    return result[(k-cur_sum) % all_food_count][1]



print(solution([3,1,2],5))
# 1 2 3 , cur_sum = 0
# 0 1 2 , cur_sum = 3
# 0 0 1 , cur_sum = 5
# k = 5 , 