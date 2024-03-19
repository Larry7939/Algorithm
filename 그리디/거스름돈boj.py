# 풀이 횟수 2

#BOJ 5585 거스름돈
import sys
paid_money = 1000
money = int(sys.stdin.readline())
coins = [500,100,50,10,5,1]
change_money = paid_money - money
answer = 0
#paid_money에서 지불해야하는 돈을 뺀 나머지(거스름돈)를 동전으로 몫 및 나머지 연산
for coin in coins:
    answer += change_money // coin
    change_money %= coin
print(answer)