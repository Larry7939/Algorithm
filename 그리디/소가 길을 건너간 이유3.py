# 선언부
N = int(input()) # N(소의 수 )
dataList = [] # dataList(도착 시간 및 검문 시간)
result = 0 

# 소가 지나갈 때마다, 지나가는 데에 소요된 시간을 체크한다.(검문 시간 계산)

# 만약 현재 소요된 시간(result)보다 도착 시간(arrivedTime)이 더 큰 경우에는,
# result와 arrivedTime의 차를 result에 더해준다.(대기 시간 계산)
for _ in range(N):
    arrivedTime, time = map(int,input().split())
    dataList.append((arrivedTime, time))
    
# 도착 시간을 기준으로 데이터 정렬
dataList.sort(key = lambda x: x[0])

result += dataList[0][0]
for data in dataList:
    if result < data[0]:
        result += (data[0] - result)
    result += data[1]
print(result)