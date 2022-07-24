#N: 행의 개수 M: 열의 개수
#행 선택
#가장 낮은 숫자 뽑아야함
#각 행에서 고를 수 있는 최악의 경우를 선택해서 최악 중 차악을 뽑는 게임이다.

#한줄 씩 입력받는 방법!
N,M = map(int,input().split())
result = 0
for i in range(N):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)
print(result)