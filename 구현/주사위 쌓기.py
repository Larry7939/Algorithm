#BOJ 2116 주사위 쌓기
import sys
from copy import deepcopy
# 아래부터 1~N번 주사위 쌓기
# 규칙:
#  서로 붙어있는 두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야한다.
#  => EX) 1번 윗면 == 2번 아랫면, 2번 윗면 == 3번 아랫면
#  단, 1번 주사위는 마음대로 놓을 수 있음
# 목표:
#  위의 규칙 하에 완성된 긴 사각기둥의 각 옆면 중 한 면의 숫자 합이 최대가 되도록 한다.
#  이를 위해 주사위를 수평방향으로 돌릴 수 있음.
# 입력:
#  주사위의 개수 / 1번 주사위부터 순서대로 입력(A,B,C,D,E,F)

# 규칙을 지키기 위해, 윗면, 아랫면에 오는 숫자가 최소가 되어야한다.
# 각 주사위의 윗면이 작은 것이 가장 중요. 
# 1번 주사위에서 가장 작은 원소 2개를 뽑고, 가장 작은 것은 윗면, 그 다음으로 작은 것은 아랫면으로 배치.
# 주사위 정보와 아랫면을 입력으로 받아서 윗면 숫자를 반환시키는 함수

# 풀이 방법 변경 ====> 첫번째 주사위로 가능한 모든 윗면,아랫면의 경우의 수를 구한 다음, 그 중에서 최댓값을 출력!
def getOpositeNum(info,index):
    if 0<index<3:
        return info[index+2]
    elif 2<index<5:
        return info[index-2]
    elif index == 0:
        return info[5]
    elif index == 5:
        return info[0]

n = int(sys.stdin.readline())
answer = []
dice_info = []
for i in range(n):
    dice_info.append(list(map(int,sys.stdin.readline().split())))
for i in range(6):
    info = deepcopy(dice_info)
    dice_sum = 0
    up_side_index = i
    up_side_value = info[0][up_side_index]
    down_side_value = getOpositeNum(info[0],up_side_index)
    info[0].remove(up_side_value)
    info[0].remove(down_side_value)
    dice_sum += max(info[0])
    for j in range(1,n):
        inner_info = deepcopy(info[j])
        down_side_value = up_side_value
        down_side_index = inner_info.index(up_side_value) #이전 주사위의 up_side_value로부터 현재 주사위의 down_side_value 생성
        up_side_value = getOpositeNum(inner_info,down_side_index)
        inner_info.remove(up_side_value)
        inner_info.remove(down_side_value)
        dice_sum += max(inner_info)
    answer.append(dice_sum)

print(max(answer))

# 1번 주사위 - 자유롭게 배치 2(아래),1(위)제외
# 3,4,5,6
# 2번 주사위 - 1,4제외
# 2,3,5,6
# 3번 주사위 - 4,3제외
# 1,2,5,6
# 4번주사위 - 3,2제외
# 1,4,5,6
# 5번주사위 - 2,6제외
# 1,3,4,5
# 6+6+6+6+5 = 29