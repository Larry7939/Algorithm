#N: 행의 개수 M: 열의 개수
#행 선택
#가장 낮은 숫자 뽑아야함
#각 행에서 고를 수 있는 최악의 경우를 선택해서 최악 중 차악을 뽑는 게임이다.

#1. 2차원 배열 초기화
#2. 각 행을 검사
#2. 각 행의 최솟값을 모아서 정렬한 후 가장 큰 것을 뽑는다.

N,M = map(int,input().split())
a = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    a[i] = list(map(int,input().split()))


m =[] #각 행의 최솟값을 모아놓은 배열
for i in range(N):
    print(a[i])
    m.append(min(a[i]))
print(max(m))