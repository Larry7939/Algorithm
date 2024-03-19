# 풀이 횟수 2
#BOJ 11399 ATM
import sys
n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))
p.sort()
#돈을 인출하는 데에 걸리는 시간을 정렬 시킨 후, 가장 작은 시간부터 누적합을 구하는 것이 핵심
sum = 0
answer = 0
for i in p:
    sum += i
    answer += sum
print(answer)

# 3 1 4 3 2
# 3 4 8 11 13 -> 39

# 1 2 3 3 4
# 1 3 6 9 13 -> 32
