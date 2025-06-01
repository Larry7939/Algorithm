N = int(input())
visited = [False] * N
broken = [False] * N
durabilities = []
weights = []
for _ in range(N):
    durability, weight = map(int,input().split())
    durabilities.append(durability)
    weights.append(weight)



# for문으로 자기 자신을 제외한 나머지 달걀들을 쳐본다.
# 이미 깨진 경우에는 치지 않는다.
# 칠 때에는 자신과 대상의 내구도를 깎는다.
max_broken_count = 0
def backtracking(idx):
    global max_broken_count
    if idx == N:
        count = 0
        for d in durabilities:
            if d <= 0:
                count += 1
        max_broken_count = max(count, max_broken_count)
        return
    if durabilities[idx] <= 0:
        backtracking(idx+1)
        return
    hit = False
    for i in range(N):
        if i == idx or durabilities[i] <= 0:
            continue
        durabilities[i] -= weights[idx]
        durabilities[idx] -= weights[i]
        hit = True
        backtracking(idx+1)
        durabilities[i] += weights[idx]
        durabilities[idx] += weights[i]
        
    if not hit:
        backtracking(idx+1)
        
backtracking(0)
print(max_broken_count)