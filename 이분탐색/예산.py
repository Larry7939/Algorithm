#BOJ 2512 예산
# 입력
n = int(input())  # 정부 개수
requests = list(map(int, input().split()))  # 각 정부에서 필요로 하는 예산
budget = int(input())  # 총 예산


# 1초에 2천만번 연산인데 제한시간은 1초이므로, 총 시간 복잡도가 2*10^7을 넘어선 안된다.
# n - 10^4
# requests - 10^5
# n^2 - 10^9으로, 2*10^7을 넘어가기 때문에, 불가
# nlogn - 10^4*10^3 = 10^7
# 이분 탐색 logn으로 풀어보자!

def calculate_needed_budget(upper_bound: int):
    # 상한액 upper_bound가 주어졌을 때, 각 정부에 필요한 예산액의 총합을 계산하는 함수
    # 함수에 들어온 상한액 후보값이 정부 예산보다 작으면 상한액으로 배정
    # 상한액 후보값이 정부 예산보다 크면 정부 예산으로 배정
    needed_budget = 0
    for request in requests:
        needed_budget += min(request, upper_bound)

    # 합을 반환
    return needed_budget

# 이분 탐색으로 상한액 탐색
low = 0
high = max(requests)
good_upper_bound = -1 #찾고자 하는 적절한 상한액
while (low <= high):
    mid = (low+high)//2
    # 함수의 반환값이 총 예산보다 작거나 같으면, 
    # 정답 후보라고 보고 good_upper_bound에 넣어준 후,
    #  #더 좋은 값을 찾기 위해 mid기준 우측을 탐색한다.
    if calculate_needed_budget(mid) <= budget:
        good_upper_bound = mid             
        low = mid+1    
    # 함수의 반환값이 총 예산보다 크면 mid기준 좌측을 탐색한다. 상한 값을 작게 잡아야 하니까.
    else:
        high = mid-1

#출력 조건 - 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.
answer = -1
for request in requests:
    given = min(request,good_upper_bound) #모든 지방은 상한액과 달라고 한 금액 중 최솟값을 받을 것이다. => 각 정부가 실질적으로 받게 되는 금액
    answer = max(answer,given) #answer에는 받은 given 중에서 최대값이 들어갈 것이다.
print(answer)