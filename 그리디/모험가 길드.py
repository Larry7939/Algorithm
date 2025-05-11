# 풀이 횟수 3
n = int(input())
data = list(map(int,input().split()))
data.sort()
group = 0 #그룹의 수
count = 0 #그룹 당 모험가 수

for fear in data:
    count += 1 #본인 포함
    if count >= fear: #구성원의 수가 현재 공포도보다 크거나 같을 시,
        group += 1 #그룹 결성 및
        count = 0 #구성원 수 초기화
print(group)