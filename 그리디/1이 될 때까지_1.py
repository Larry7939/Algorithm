# 풀이 횟수 2
# N%K!=0일 때 or ==0일 때
# N을 1로 만드는 1,2번 과정의 최소 필요 횟수

#내가 생각하는 풀이 방법
#1. 나누기를 최대한 많이 해서 N의 크기를 줄인 다음, 2번 연산을 하는 방법

N=0
K=0
count=0

N,K = map(int,input().split())

while N!=1:
    if N%K==0:
        N = N//K
        count = count+1
    else:
        N = N-1
        count = count+1
print(count)

# result = N//K + N%K
# print(result)


