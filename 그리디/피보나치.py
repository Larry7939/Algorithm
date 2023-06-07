# 0 1 1 2 3 5 8 13 21 34 55 89 144
import sys

def getFibonacci(n: int) -> list:
    i = 0
    fibo = [0, 1]
    while fibo[-1] < n:
        fibo.append(fibo[i]+fibo[i+1])
        i += 1
    return fibo

sum_list = []
fibo_list = []
answer = []
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    fibo_list = getFibonacci(n)
    fibo_list.sort(reverse=True)
    for f in fibo_list:
        if f<=n:
           answer.append(f)
           n -= f
           if n == 0:
               print(*answer[::-1])
               answer = []
               break 
# 1. 입력된 수 이하의 원소들을 갖고있는 피보나치 수열 만들기
# 2. 피보나치 수열 원소 중 가장 크고, 입력된 수보다는 작은 원소를 따로 저장하기
# 3. 입력된 수에서, 위에서 구한 원소를 빼기.
# 4. 뺀 결과로 2~3번 과정 반복

