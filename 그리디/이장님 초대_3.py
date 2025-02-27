#BOJ 9237 이장님 초대

# 묘목의 수 N 입력
# 묘목이 성장하는 데에 걸리는 시간 리스트 growthList 입력

N = int(input())
growthList = list(map(int,input().split()))
result = 0


# 전제 조건 1:
# 자라는 데에 가장 오래 걸리는 묘목을 먼저 심어야한다.
# -> 내림차순 정렬
growthList.sort(reverse=True)

# 전제 조건 2:
# 심는 데에 걸리는 시간(1일)을 고려하여, 리스트의 모든 원소를 성장에 걸리는 시간으로 변환한다.
# -> 인덱스 + 1만큼을 추가
for n in range(0, len(growthList)):
    growthList[n] += (n+1) 

# 결론:
# 그 중 최댓값 + 1을 출력한다.
print(max(growthList) + 1)


# 모든 묘목을 자라게 할 수 있는 가장 빠른 날짜 출력

