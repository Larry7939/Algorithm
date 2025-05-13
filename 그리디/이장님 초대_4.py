n=int(input())
trees= list(map(int,input().split()))
trees.sort(reverse=True)

# 묘목을 역순 정렬하여, 가장 오래 걸리는 것부터 심는다.
# 모든 묘목에 심는데까지 걸리는 시간을 포함하여 더한다.
# 즉, 각 묘목마다 더해지는 시간이 다르다.

# 5 5 6 6
# => 4 3 3 2

# 39 39 38 35 20 9
# => 40 41 41 39 25 15

for i in range(0, n):
    trees[i] += (i+1)
print(max(trees) + 1) # 심고 난 다음 날 이장님 방문하므로 + 1
