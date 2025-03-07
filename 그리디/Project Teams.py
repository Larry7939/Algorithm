N = int(input())
stats = list(map(int,input().split()))
result = []
stats.sort()
for i in range(len(stats)):
    result.append(stats[i] + stats[len(stats)-i-1])
print(min(result))

# 핵심: 가장 큰 역량과 작은 역량을 짝지어야 한다.