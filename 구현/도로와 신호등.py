# BOJ 2980 도로와 신호등
import sys

# 1초에 1미터씩 이동
# 도로의 시작은 0, 끝은 L미터 지점
# 빨간색 - 초록색으로 바뀔 때까지 기다린다.

lights = dict([])
time = 0
# 입력
#  N:신호등의 개수, L:도로의 길이
#  D:신호등의 위치, R:빨간색 지속 시간, G:초록색 지속시간
N, L = map(int, sys.stdin.readline().split())
for _ in range(N):
    D, R, G = map(int, sys.stdin.readline().split())
    lights[D] = [R, G]

# 모든 순간, 모든 신호등의 초가 흐르며 신호도 바뀐다.
# 현재 소요 시간으로 해당 신호등의 신호를 알 수 있어야한다.
# 현재 소요 시간을, 해당 신호등의 총 신호(빨간,초록) 시간으로 나눈다.
# 위에서 나눈 나머지 값이 빨간 신호 시간보다 크면, 초록 신호이므로 지나간다.
# 위에서 나눈 나머지 값이 빨간 신호 시간보다 작으면, 빨간 신호이므로, 빨간신호 시간에서 위에서 나눈 나머지 값을 뺀 시간을 기다린다. (answer += time)


def process_light_time(time: int, lights: dict, location: int) -> int:
    r_time = lights[location][0]
    result = time % sum(lights[location])
    if result < r_time:
        time += r_time - result
    return time

# 반복문으로 i를 0부터 L까지 반복한다.
# 변수 time - 이동 시간
# i가 신호등의 위치와 일치하면, 위 로직을 수행한다.
# 일치하지 않으면, time을 증가시킨다.
for i in range(L):
    if i in lights.keys():
        time = process_light_time(time, lights, i)
    time += 1

# 출력
#  상근이가 도로의 끝까지 이동하는 데에 걸리는 시간 출력
print(time)