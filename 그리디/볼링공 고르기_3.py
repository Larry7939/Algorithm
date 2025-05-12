m,n = map(int,input().split())
weights = list(map(int,input().split()))
count = 0

# 2중 for문으로 weights[i] != weights[j]인 경우 count +=1

for i in range(n):
    for j in range(n):
        if weights[i] != weights[j] and i != j:
            count += 1

print(count//2)