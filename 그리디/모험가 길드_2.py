# 5, 1 2 2 2 3 -> 2
# 9, 2 2 2 2 2 2 2 2 3 -> 4
# 6, 4 2 1 2 3 2 -> 2

# N: 인원 수 입력
N = int(input())
# fear_list: 공포도 리스트 입력
fear_list = list(map(int,input().split()))
# 공포도 정렬
fear_list.sort()
# 맨 앞부터 카운트 된 인원 수와 현재 공포도가 일치하는 지 체크
count = 0
group = 0
for fear in fear_list:
    count += 1
    #  그룹 결성 및 카운트, 인원 수 초기화
    if fear == count:
        group += 1
        count = 0
        
# 그룹 수 출력
print(group)
    
 