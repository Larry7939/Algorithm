#BOJ 7568 덩치
# 덩치는 (몸무게, 키)로 표현된다.

# 각 사람의 덩치 등수 - 자신보다 더 큰 덩치의 사람 수로 정해진다.
# 같은 덩치 등수 여러 명 가능

# N : 전체 사람의 수
# wh_list : 덩치 리스트

# 맨 앞에서부터 자신보다 몸무게와 키 모두 큰 사람의 수 k를 구하고, +1한 것이 본인의 등수임.
wh_list = []
N = int(input())
for _ in range(N):

    wh_list.append(list(map(int,input().split())))

rankings = []
for wh in wh_list:
    rank = 1
    for i in range(N):
        if wh[0] < wh_list[i][0] and wh[1] < wh_list[i][1]:
            rank += 1
    rankings.append(rank)
print(*rankings)
# 순서대로 덩치 등수 출력