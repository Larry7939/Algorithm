N = int(input())
waiting = list(map(int,input().split()))
waiting.sort()
result = 0
for i in range(N):
    result += waiting[i]*(N-i)
print(result)