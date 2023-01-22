# BOJ 3090 차이를 최소로
# 입력부
# 배열 a의 크기 n 입력
# 감소연산 최대 횟수 t 입력

n, t = tuple(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
# left < right인 경우, 원소간의 차이를 좁히기 위한 감소현산 - O(n)
# left > right인 경우, 원소간의 차이를 좁히기 위한 감소현산 - O(n)

def needed_num_operation(x: int) -> int:
    b = a[:]
    num_operation = 0
    for i in range(n-1):
        if b[i+1] - b[i] > x:
            num_operation += b[i+1]-b[i]-x
            b[i+1] = b[i] + x
    for i in range(n-1, 0, -1):
        if b[i-1] - b[i] > x:
            num_operation += b[i-1]-b[i]-x
            b[i-1] = b[i] + x
    return num_operation
# 이분탐색
# 최소 차이 : 0
# 최대 차이 : 배열의 max 값
low = 0
high = max(a)
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
