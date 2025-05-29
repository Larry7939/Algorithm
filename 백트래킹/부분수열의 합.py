N, S = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
count = 0

def backtracking(index, current_sum):
    global count
    if index == N:
        if current_sum == S:
            count += 1
        return
    # 고르는 경우
    backtracking(index+1, current_sum + a[index])
    # 고르지 않는 경우
    backtracking(index+1, current_sum)
backtracking(0,0)
if S == 0:
    count -=1
print(count)