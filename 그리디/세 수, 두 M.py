import sys


def f(a, b, c):
    # 평균x3 = a + b + c
    # 중앙값x3 = 3*b
    return abs(a + b + c - 3 * b)


N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

A.sort()

answer = -1
for i in range(1, N-1):
    # 중앙값이 A[i]인 경우
    answer = max(answer, f(A[i-1], A[i], A[N-1]))  # 평균이 최대인 경우
    answer = max(answer, f(A[0], A[i], A[i+1]))  # 평균이 최소인 경우
print(answer)
