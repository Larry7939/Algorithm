n = int(input())
waitings = list(map(int,input().split()))
waitings.sort()
totalWatingTime = 0
for i in range(0,len(waitings)):
    totalWatingTime += sum(waitings[:i+1])
print(totalWatingTime)