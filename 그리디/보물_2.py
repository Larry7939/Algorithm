# 풀이 횟수 2
#BOJ 1026 보물

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
result = 0
for i in range(N):
    result += A[i] * B[i]
print(result)