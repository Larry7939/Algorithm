#BOJ 2290 LCD Test
#7 segments 참조 링크 - https://omjinlts.github.io/algorithm/2290/
import sys

h, v = '-', '|'
s, n = sys.stdin.readline().split()
s = int(s)

# 가로 s+2, 세로 2s+3
# 7-segment
# 숫자마다 특정 segment를 포함하는지 확인 한 후, '-' 혹은 '|' 출력

def construct_segment(n):
    lcd = [[' ']*(s+2) for _ in range(2*s+3)] #숫자 하나를 출력하기 위한 배열
    for i in range(1,s+1):
        if n in '02356789': # a
            lcd[0][i] = h
        if n in '01234789': # b
            lcd[i][-1] = v
        if n in '013456789' : #c
            lcd[s+1+i][-1] = v
        if n in '0235689': #d
            lcd[2*s+2][i] = h
        if n in '0268':#e
            lcd[s+1+i][0] = v
        if n in '045689':#f
            lcd[i][0] = v
        if n in '2345689':#g
            lcd[s+1][i] = h
    return lcd

display = [construct_segment(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r),end=' ')
    print()
