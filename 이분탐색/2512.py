#BOJ 2512 예산
# 입력
n = int(input())  # 정부 개수
requests = list(map(int, input().split()))  # 각 정부에서 필요로 하는 예산
budget = int(input())  # 총 예산

def calculate_needed_budget(upper_bound: int):
    # 상한액 upper_bound가 주어졌을 때, 각 정부에 필요한 예산액의 총합을 계산하는 함수

    needed_budget = 0
    for request in requests:
        needed_budget += min(request, upper_bound)
    return needed_budget

# 이분 탐색을 수행하는 메인 로직
low = 0
high = max(requests)
good_upper_bound = -1 #찾고자 하는 적절한 상한액
while (low <= high):
    mid = (low+high)//2
    if calculate_needed_budget(mid) <= budget: #총 예산보다 작거나 같으면 적절한 정답 후보라고 보고
        good_upper_bound = mid                 #good_upper_bound에 넣어준다.
        low = mid+1                            #더 좋은 값을 찾기 위해 탐색 범위를 바꿔준다.
    else:
        high = mid-1

#출력 조건 - 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.
answer = -1
for request in requests:
    given = min(request,good_upper_bound) #모든 지방은 상한액과 달라고 한 금액 중 최솟값을 받을 것이다. => 각 정부가 실질적으로 받게 되는 금액
    answer = max(answer,given) #answer에는 받은 given 중에서 최대값이 들어갈 것이다.
print(f"상한액 - ${good_upper_bound}")
print(f"answer - ${answer}")