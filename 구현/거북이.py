#BOJ 8911 거북이
import sys
#입력
n = int(sys.stdin.readline())

#F:한칸 앞
#B:한칸 뒤
#L:왼쪽 90도 회전
#R:오른쪽 90도 회전

#시작지점 - 0,0 / 시작방향 - 북쪽
start = 0,0
directions = ['N','E','S','W'] #북동남서
answer = []
#지나간 영역을 사각형으로 만들기 위해 x,y좌표 각각을 추가

#direction, cur_direction을 매개변수로 하는 방향전환 함수 
def changeDirection(direction:str,cur_direction:int):
    if direction == 'L':
        cur_direction -=1
        if cur_direction == -1:
            cur_direction = 3
    elif direction == 'R':
        cur_direction = (cur_direction + 1)%4
    return cur_direction

# 좌우 방향, 진행 방향, 현재 좌표를 매개변수로 하는 이동 함수
def move(direction,way,x,y):
    d = directions[direction]
    if d == 'N':
        if way == 'F':
            y+=1
        elif way == 'B':
            y -= 1

    elif d== 'E':
        if way == 'F':
            x+=1
        elif way == 'B':
            x-=1
    elif d== 'S':
        if way == 'F':
            y-=1
        elif way == 'B':
            y+=1
    elif d== 'W':
        if way == 'F':
            x-=1
        elif way == 'B':
            x+=1
    x_pos.append(x)
    y_pos.append(y)
    return x,y
#지나간 영역을 포함하는 사각형의 넓이
def cal_area():
    x = max(x_pos)-min(x_pos)
    y = max(y_pos)-min(y_pos)
    return x*y

for _ in range(n):
    x,y = start
    direction = 0
    x_pos = [0]
    y_pos = [0]
    steps = list(sys.stdin.readline().rstrip())
    for step in steps:
        if step == 'L' or step == 'R':
            direction = changeDirection(step,direction)
        elif step=='F' or step=='B':
            x,y = move(direction,step,x,y)
    area = cal_area()
    answer.append(area)
for a in answer:
    print(a)

#단순 방향 시뮬레이션 문제