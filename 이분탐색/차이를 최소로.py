# BOJ 3090 차이를 최소로
# 입력부
# 배열 길이 n - 10^5
# 감소연산 횟수 t - 10^9
# 각 원소의 차이 - 10^9
# 배열 a

n, t = tuple(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))

# 시간제한 1초
# n^2 - 10^14으로, 10^7*2보다 크다. fail
# nlogn - 10^5*10*3 = 3*10^6으로, 10^7*2보다 작다
# 이분탐색을 활용하여 문제를 풀어보자!
# 이분탐색 내부에서 조건에 따라 감소연산을 하는 함수를 호출 해야 한다!

# left < right인 경우, 원소간의 차이를 좁히기 위한 감소현산 - O(n)
# left > right인 경우, 원소간의 차이를 좁히기 위한 감소현산 - O(n)

def needed_num_operation(x: int) -> int:
    b = [a[i] for i in range(n)]
    num_operation = 0
    # 우측이 좌측보다 큰 경우 감소연산하고 감소연산 횟수 카운트
    for i in range(n-1):
        if b[i+1] - b[i] > x:
            num_operation += b[i+1]-b[i]-x
            b[i+1] = b[i] + x
    for i in range(n-1, 0, -1):
    # 좌측이 우측보다 큰 경우 감소연산하고 감소연산 횟수 카운트
        if b[i-1] - b[i] > x:
            num_operation += b[i-1]-b[i]-x
            b[i-1] = b[i] + x
    return num_operation

# 이분탐색
# 최소 차이 : 0
# 최대 차이 : 10^9 - 각 원소의 최대 차이
low = 0
high = int(1e9)
answer = -1

while low <= high:
    mid = (low+high)//2
    if(needed_num_operation(mid) <= t): #입력된 최대 횟수보다 감소 연산을 조금만 사용한 것이므로, 최대한 차이를 좁히기 위해 몇번 더 연산 사용
        answer = mid
        high = mid-1
    else:
        low = mid + 1 #차이를 좁게 하려니 연산 횟수를 초과했으므로, 차이를 보다 널널하게 잡기


for i in range(n-1):
    if a[i+1] - a[i] > answer:
        a[i+1] = a[i] + answer
for i in range(n-1, 0, -1):
    if a[i-1] - a[i] > answer:
        a[i-1] = a[i] + answer
print(" ".join(list(map(str,a))))
# 총 예산 시간 복잡도 - O(nlogn)
# 각 인접한 수의 차이가 x가 되도록 하는 연산의 최소 횟수를 이분탐색으로 구하고,
# 해당 연산 횟수가 입력받은 횟수인지를 체크하면 된다.
