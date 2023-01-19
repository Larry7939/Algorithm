# BOJ 1300 K번째 수
# 이차원 배열을 만들고 이걸 읽어서 1차원 배열로 만드는 것은 시간/공간복잡도 측면에서 O(N^2)이기 때문에, 너무 비효율적이다.
# K번째 수의 조건을 만족하는지를 조건 이분탐색 하기 위하여 각 행마다 타겟보다 작은/큰 값의 개수를 전부 더해서 반환한다.
# K번째 수의 조건이란? -> 배열의 크기가 n일 때, k번째 수는 k번째 수보다 작은 수의 개수가 k-1개 이하이고 큰 수의 개수가 n-k개 이하여야한다.
n = int(input())
k = int(input())

# x보다 작은 수의 개수를 전부 세는 함수
def get_num_smaller(x: int):
    num_smaller = 0
    for i in range(1, n+1):
        num_smaller += min(n, (x-1)//i)
    return num_smaller
# x보다 큰 수의 개수를 전부 세는 함수 : (n - (x보다 작거나 같은 수의 개수))
def get_num_bigger(x: int):
    num_bigger = 0
    for i in range(1, n+1):
        num_bigger += n - min(n, x//i)
    return num_bigger

low = 1
high = min(n*n, int(1e9))
answer = -1

while low <= high:
    mid = (low+high)//2
    # mid(k번째 수)보다 작은 수의 개수가 k-1보다 많으면, mid가 너무 큰 것이므로 high = mid-1
    if get_num_smaller(mid) > k-1:
        high = mid - 1
    # mid(k번째 수)보다 큰 수의 개수가 n-k보다 많으면, mid가 너무 작은 것으므로 low = mid+1
    elif get_num_bigger(mid) > n*n-k:
        low = mid + 1
    # else : k번째 수의 조건을 만족하므로, 이분 탐색을 멈추고 answer = mid
    else:
        print(mid)
        answer = mid
        break
print(answer)