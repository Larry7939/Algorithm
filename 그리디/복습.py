import sys
#모험가 길드

n = int(sys.stdin.readline())
fear_list = list(map(int,sys.stdin.readline().split()))
fear_list.sort()
#공포도가 낮은 모험가부터 그룹 결성
#공포도보다 구성원 수가 크거나 같아지면 그룹 결성
count = 0
group_count = 0
for fear in fear_list:
    count += 1
    if fear <= count:
        group_count += 1
        count = 0

print(group_count)

# 공포도가 낮은 모험가부터 그룹을 결성하는 것이 핵심