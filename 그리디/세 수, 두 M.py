import sys


def f(a, b, c):
    return abs(a + b + c - 3 * b)


N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

A.sort()

answer = -1
for i in range(1, N-1):
    answer = max(answer, f(A[i-1], A[i], A[N-1]))
    answer = max(answer, f(A[0], A[i], A[i+1]))
print(answer)
