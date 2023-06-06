#BOJ 1026 보물
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

result = 0

# b의 최댓값에 a의 최솟값을 곱해서 result에 더한다.

for _ in range(n):
    min_a = min(a)
    max_b = max(b)
    result += min_a * max_b
    a.remove(min_a)
    b.remove(max_b)
print(result)