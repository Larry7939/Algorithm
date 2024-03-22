#BOJ 9237 이장님 초대

# 묘목의 수 N 입력
# 성장 시간 리스트 T 입력
N = int(input())
T = list(map(int,input().split()))
T.sort(reverse = True)
result = []
for i in range(N):
    result.append(T[i] + i)
print(max(result)+2)
# 성장 시간을 큰 순서대로 정렬
# 성장 시간 + 인덱스(이전 나무들을 심는 데에 걸린 시간)을 배열에 append
# 배열을 큰 순서대로 정렬
# 최댓값 + 2 출력(묘목을 구입한 날 + 마지막 나무가 다 자란 다음 날 이장님 초대)