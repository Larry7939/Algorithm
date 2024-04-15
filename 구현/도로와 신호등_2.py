# BOJ 2980 도로와 신호등

# N: 신호등의 개수
# L: 도로의 길이
N, L = map(int,input().split())
# D,R,G (신호등 위치, 빨간색 지속시간, 초록색 지속시간)
traffic_lights = []
for _ in range(N):
    traffic_lights.append(list(map(int,input().split())))
# 다음 신호등까지 이동 -> 신호등 위치 - 현재 위치의 절대값을 total_ellapsed_time에 더한다.
# 현재 신호(R or G)가 초록불인지 확인 ->  지금까지 소요된 시간을 (R+G)로 나머지 연산하면, 현재 신호등의 신호 인덱스를 알 수 있음.
current_location = 0
total_ellapsed_time = 0
for light in traffic_lights:
    light_location = light[0]
    total_ellapsed_time = total_ellapsed_time + abs(light_location-current_location) #현재 신호등까지 이동하는 데에 걸리는 시간 합산
    current_location = light_location #현재 위치 갱신
    red_time = light[1]
    green_time = light[2]
    current_light_time = total_ellapsed_time % (red_time + green_time)
    if current_light_time <= red_time:
        total_ellapsed_time += abs(red_time-current_light_time) # 빨간불인 경우, 대기

total_ellapsed_time = total_ellapsed_time + L-current_location # 목적지까지 이동하는 데에 걸리는 시간 합산
print(total_ellapsed_time)
