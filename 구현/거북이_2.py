#BOJ 8911 거북이
# t: 테스트 케이스의 수
# case: 각 테스트 케이스마다 F,B,L,R 문자 배열이 입력된다. 앞으로, 뒤로, 왼쪽 90도 회전, 오른쪽 90도 회전
t = int(input())


# 거북이의 현재 좌표
current_location = [0,0]
# 거북이의 동선 좌표를 담을 x배열과 y배열
x_history = [0]
y_history = [0]
# 초기 방향 - 북쪽
direction = 3 
# 0:동, 1:남, 2:서, 3:북
# 동서남북 방향 백터
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for _ in range(t):
    case = input()
    for c in case:
        if c == "L":
            if direction == 0:
                direction = 3
            else:
                direction = (direction - 1) % 4
        elif c == "R":
            direction = (direction + 1) % 4
        elif c == "F":
            current_location[0] += dx[direction]
            current_location[1] += dy[direction]
            x_history.append(current_location[0])
            y_history.append(current_location[1])
        elif c == "B":
            current_location[0] -= dx[direction]
            current_location[1] -= dy[direction]
            x_history.append(current_location[0])
            y_history.append(current_location[1])
    width = abs(max(x_history) - min(x_history))
    height = abs(max(y_history) - min(y_history))
    print(width * height)
    current_location = [0,0]
    x_history.clear()
    y_history.clear()








# 거북이가 지나간 영역의 x좌표 중 최댓값과 최솟값의 차(절대값)
# 거북이가 지나간 영역의 y좌표 중 최댓값과 최솟값의 차(절대값)
# 위 두 수를 곱하면 된다.

# => 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이 출력