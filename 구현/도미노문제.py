import sys
sys.setrecursionlimit(10**6)
from itertools import combinations
def solution(position, height, m):
    result = []

    n = len(position)
    a = combinations(position,m) #제거할 블록 m개 선정
    for i in a:
        destroyed_nums = 0
        is_destroyed = [False]*(n+1)
        temp = list(set(position)-set(i))
        temp.sort()
        needed_position = temp # 블록 m개를 뽑아서 제거
        result.append(get_destroyed(m,destroyed_nums,is_destroyed,needed_position,height)) # m개가 제거된 블록들로 불안정도의 최댓값을 구한다.
    answer = min(result)
    return answer

# 좌표 x, 높이 h인 블록이 넘어지면 x~x+h에 있는 모든 블록 넘어짐
# 불안정도 - n개의 블록 중 하나가 넘어졌을 때, 추가적으로 넘어지는 블록 개수의 최댓값
# m개를 제거해서 얻을 수 있는 불안정도의 최솟값

# 전체 도미노 블록에서 combinations로 2개를 뽑아서 제외한 다음,
# 남아있는 도미노 블록들로 get_destoryed(num)을 for문을 돌려서 그 중 최댓값을 뽑아서
# 불안정도 들을 구하자.
# 그 다음에 불안정도 중에서 최솟값을 뽑으면 된다.
#num번째 블록이 넘어졌을 때 연쇄적으로 넘어지는 블록 개수 반환
def get_destroyed(m,destroyed_nums,is_destroyed,positions,height): 
    n = len(positions)
    max_destroyed = []
    for i in range(n): # 최초 무너짐
        for j in range(i+1,n):
            if positions[i] < positions[j] and positions[j] <= positions[i]+height[i]:
                is_destroyed[j] = True
                destroyed_nums += 1

        for k in is_destroyed: # 연쇄적으로 무너짐
            if k == True and m == 0:
                destroyed_nums += 1
        max_destroyed.append(destroyed_nums)
        destroyed_nums = 0
        is_destroyed = [False]*(n+1)
    return max(max_destroyed)


#positions 배열을 2중 for문으로 검사해서 
#positoins[j]가 positions[i]보다 크고(오른쪽에 있고)
#positoins[j]가 positions[i]+hegiht[i]보다 작거나 같으면
#무너뜨린다.
#is_destroyed를 검사해서 True인 것들에 대해서만
#재귀함수를 돌려 연쇄로 무너뜨린다.
