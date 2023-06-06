#BOJ 11497 통나무 건너뛰기
from collections import deque
import sys
# 10 10 11 11 12 12 13
# 10 10 12 13 12 11 11

# 2 4 5 7 9
# 2 5 9 7 4

#가장 최대 난이도가 낮은 구조는, 최댓값이 가운대로 오고 좌우로 펼쳐지는 형태.
#원본 배열과, 좌우로 펼쳐지는 형태는 아래와 같은 관계가 있다.
# 최댓값(woods[0])과 woods[1], 최댓값(woods[0])과 woods[2] 중에서 큰 값 구하기
# 원본 배열 기준, 2,4,6,8~~ 짝수번째 수 끼리 이동 => 좌우로 펼쳐지는 형태에서 가운데로부터 좌측으로 이동
# 원본 배열 기준, 1,3,5,7~~ 홀수번째 수 끼리 이동 => 좌우로 펼쳐지는 형태에서 가운데로부터 우측으로 이동
# 각 차이의 최대값을 출력

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    woods = list(map(int, sys.stdin.readline().split()))
    woods.sort()
    max_diff = max(woods[1]-woods[0], woods[2]-woods[0])

    for i in range(1, n-2):
        max_diff = max(max_diff, woods[i+2]-woods[i])
    for i in range(2, n-2):
        max_diff = max(max_diff, woods[i+2]-woods[i])

    print(max_diff)