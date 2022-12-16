a = list(map(int,input().split()))
n = len(a)
sum = 0
for i in a:
    sum +=i
print("%d %.2f"%(sum,sum/n))
