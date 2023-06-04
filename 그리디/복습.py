import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    cur_sum = 0
    before_food = 0
    all_food_count = len(q)

    # 지금까지 소모된 시간(cur_sum) + 이제 소모될 시간(q[0][0]-before_count) * all_food_count)이 k보다 작거나 같을 때에만!
    # 즉, 모든 음식에 공평하게 사이클을 돌 수 있을 때에만 수행된다.

    #q[0][0]에서 before_food를 빼는 이유는, 사이클을 돌기 때문에, before_food를 소모할 때 q[0][0]도 함께 소모했기 때문이다!!
    while cur_sum + (q[0][0] - before_food) * all_food_count <= k:
        now_food = heapq.heappop(q)
        cur_sum += (now_food[0] - before_food) * all_food_count
        all_food_count -= 1
        before_food = now_food[0]

    #while문을 빠져나왔다는 것은, 소모 시간이 k보다 커지기 때문에, 더 이상 전체를 순회하지 못한다는 의미이다.
    result = sorted(q,key=lambda x: x[1])
    return result[(k-cur_sum) % all_food_count][1] #인덱스 반환

# 우선순위 큐를 사용하여 가장 소모 시간이 짧은 음식을 기준으로 사이클을 도는 개념이 핵심
# 사이클을 돌아야 한꺼번에 여러 음식의 수를 빠르게 줄일 수 있음. 즉, 여러 음식을 먹는 시간을 빠르게 잴 수 있음