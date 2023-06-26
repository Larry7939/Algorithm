#BOJ 톱니바퀴(2) 15662
import sys
from collections import deque
#일렬로 놓인 T개의 톱니바퀴
#각 톱니는 N(0)극 or S(1)극 중 하나를 나타낸다.
#맨 왼쪽 톱니바퀴는 1번~~ 마지막은 T번
#톱니바퀴를 K번 회전(한 칸 회전, 시계방향(1) OR 반시계방향(-1))
# 회전 시, 서로 맞닿은 극에 따라, 옆의 톱니바퀴를 회전시킬 수도, 그렇지 않을 수도 있다.
# 만약 A와 B 톱니바퀴의 맞닿은 톱니의 극이 다르다면, B는 A의 회전방향과 반대 방향으로 회전한다.
# 만약 A와 B 톱니바퀴의 맞닿은 톱니의 극이 같다면, B는 회전하지 않는다.

#회전 방향에 따라 appendleft(pop()) 또는 append(popleft())를 활용
#중요한 톱니는 맞닿게 되는 2번째와 6번째 톱니.
# 현재 바퀴 기준 오른쪽으로 간다면, 현재 2번째와 다음 바퀴의 6번째 톱니를 비교해야함.
# 현재 바퀴 기준 왼쪽으로 간다면, 현재 6번째와 다음 바퀴의 2번째 톱니를 비교해야함.
# 만약 톱니의 극이 다르다면, 해당 기어에 대해서도 rotate함수 재귀호출
# 만약 현재 바퀴가 마지막 바퀴이거나, 톱니의 극이 같다면, 호출하지 않음.
def decideDirection(gears,gear_num, rotate_direction): #톱니바퀴 정보, 톱니바퀴 번호, 회전 방향을 매개변수로 하는 회전함수
    if gear_num == T: #현재 바퀴가 T번째인 경우 - 왼쪽으로 진행
        rotate(gears,gear_num,-1,rotate_direction) #회전함수 호출
    elif gear_num == 1: #현재 바퀴가 1번째인 경우 - 오른쪽으로 진행
        rotate(gears,gear_num,1,rotate_direction) #회전함수 호출
    else:
        if gear_num == 1 or gears[gear_num][6] == gears[gear_num-1][2]:
            pass
        else:
            rotate(gears,gear_num-1,-1,-rotate_direction) #회전함수 호출

        if gear_num == T or gears[gear_num][2] == gears[gear_num+1][6]:
            pass
        else:
            rotate(gears,gear_num+1,1,-rotate_direction) #회전함수 호출

        if rotate_direction == 1: #시계방향
            gears[gear_num].appendleft((gears[gear_num].pop()))
        elif rotate_direction == -1: #반시계방향
            gears[gear_num].append((gears[gear_num].popleft()))


def rotate(gears,gear_num,direction,rotate_direction):
    if direction == -1: #왼쪽
        if gear_num == 1 or gears[gear_num][6] == gears[gear_num-1][2]:
            pass
        else:
            rotate(gears,gear_num-1,direction,-rotate_direction) #극이 다르면 방향을 바꿔서 회전

    elif direction == 1: #오른쪽
        if gear_num == T or gears[gear_num][2] == gears[gear_num+1][6]:
            pass
        else:
            rotate(gears,gear_num+1,direction,-rotate_direction)

    if rotate_direction == 1: #시계방향
        gears[gear_num].appendleft((gears[gear_num].pop()))
    elif rotate_direction == -1: #반시계방향
        gears[gear_num].append((gears[gear_num].popleft()))


#입력 - 톱니바퀴 T개의 초기 상태와 회전 방법
# 톱니 바퀴의 개수 T개
# 톱니 바퀴의 상태 - 8개의 정수로 이루어져있고, 12시 방향부터 시계방향 순서대로 주어진다.
# N극 - 0, S극 - 1
# 회전 횟수 K
# 회전 방법(회전시킨 톱니바퀴의 번호, 방향(1:시계방향,-1:반시계방향))
T = int(sys.stdin.readline())
gears = dict()
for i in range(1,T+1):
    tooth_info = deque(list(sys.stdin.readline().rstrip()))
    gears[i] = tooth_info
K = int(sys.stdin.readline())
for _ in range(K):
    gear_num,direction = map(int,sys.stdin.readline().split())
    # gear_num 기준으로 좌우에 존재하는 톱니바퀴에 대해서 회전함수 호출
    decideDirection(gears,gear_num,direction)

answer = 0
#출력 - 총 K번 회전시킨 후, 12시 방향이 S극인 톱니바퀴의 개수 출력
for i in gears.values():
    if i[0] == '1':
        answer+=1
print(answer)


# 재귀를 활용하는 아이디어, 회전 조건을 잘 파악하고 회전을 좌/현재/우로 나누어 동작시키는 것이 핵심
