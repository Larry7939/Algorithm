import sys
# 1이 될 때까지
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.

n,k = map(int,sys.stdin.readline().split())
result = 0

# while문을 돌면서 n이 k로 나누어 떨어지면 2번, 그렇지 않으면 1번을 수행한다.
while n != 1:
    if n % k == 0:
        n = n//k
        result += 1
    else:
        result += n%k
        n -= n%k
        
print(result)
# 1번 과정보다는 2번 과정을 최대한 많이 수행하여, 빠르게 N을 감소시키는 것이 핵심