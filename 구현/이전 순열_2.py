# BOJ 10973 이전순열
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 더 작은 순열을 만들어야하기 때문에, 큰 수가 앞에 배치된 것이 있는지 확인한다.
# 찾았다면, 해당 인덱스를 target에 저장한다.
# 찾지 못한다면, 이보다 더 작은 순열은 없는 것이므로, -1을 출력하고 종료한다.
x = False
for i in range(n-1, 0, -1):
    if a[i-1] > a[i]:
        x = True
        target = i-1
        break
if x == False:
    print(-1)
    sys.exit(0)

for i in range(n-1, target-1, -1):
    if a[target] > a[i]:
        temp = a[target]
        a[target] = a[i]
        a[i] = temp
        a = a[:target+1] + sorted(a[target+1:], reverse=True)
        break
print(*a)
# 5 3 1 2 4
# 5 2 4 3 1

# 5 3 4 1 2
# 5 3 2 4 1

# 인덱스 n-1부터 1씩 내려오면서 원소를 체크한다.
# 바로 직전 순열을 찾기 위해선, 앞의 수보다 뒤의 수가 더 큰 모습이 되어야한다.
