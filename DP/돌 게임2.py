n = int(input())
dp = [False] * (n + 1)

# 돌 1개: 내가 가져가야 되니까 -> 지는 상태
# 돌 2개: 1개만 가져가면 상대가 마지막 가져감 -> 이기는 상태
# 돌 3개: 다 가져가면 상대 돌 없음 -> 이기는 상태

dp[1] = False  # 지는 상태
if n >= 2: dp[2] = True   # 이김
if n >= 3: dp[3] = True   # 이김

for i in range(4,n+1):
    if not dp[i-3] or not dp[i-1]:
        dp[i] = True
        
if dp[n]:
    print("SK")
else:
    print("CY")