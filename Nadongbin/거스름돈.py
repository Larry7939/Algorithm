#500원짜리를 최대한 많이 줘야한다.
#기준은 가치가 큰 동전부터!
#10의 배수 N에 대해서 500부터 순서대로 10까지 나눈 몫을 다 더한 값을 구하면 된다.

coins = [500,100,50,10]
n = 0 #동전의 개수 n
result = 0 #나눗셈 계산의 결과
N =int(input("금액을 입력하세요: "))
for i in coins:
    n += N//i
    N = N%i
print(f"동전의 개수 : {n}개")



