import heapq
# food_times: 음식을 먹는 데 필요한 시간 리스트
# k: 네트워크 장애 발생 시간

# 3 1 2
# 1초 - 2 1 2, index = 0
# 2초 - 2 0 2, index = 1
# 3초 - 2 0 1, index = 2
# 4초 - 1 0 1, index = 0
# 5초 - 1 0 0, index = 2

# q에 (섭취 시간,인덱스) 형태로 저장 
# 만약 장애 발생 전에 모든 음식을 먹는 경우 -1 반환
# 가장 섭취 시간이 짧은 음식을 기준으로 우선 섭취
# 한 번 사이클을 돌 수 있을 때에만 while문 수행하며 한꺼번에 수행
# 현재까지 소모된 시간(total_time) + 이번에 소모할 시간(q[0][0] - before_food)*all_food_count가 k보다 작거나 같은 동안 수행
# q[0][0]는 이번에 섭취할 음식, before_food를 빼는 이유는, 이전 음식을 먹을 때 이미 이번에 섭취할 음식의 시간도 함께 섭취했기 때문임.

def solution(food_times,k):
    q = []
    food_count = len(food_times)
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i],i+1))
    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    total_time = 0
    before_food_time = 0
    
    while total_time + (q[0][0] - before_food_time) * food_count <= k:
        now_food = heapq.heappop(q)
        total_time += now_food[0] * food_count
        before_food_time = now_food[0]
        food_count -= 1
    # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
    result = sorted(q, key = lambda x: x[1])
    print((k-total_time) % food_count)
    print(result[(k-total_time) % food_count][1])
    return result[(k-total_time) % food_count][1]
print(solution([3,1,2],5))