def showStatus():
    for i in range(h):
        print(*MAP[i])


h, w = map(int, input().split())
MAP = [[0]*w for _ in range(h)]
n = int(input())

for _ in range(n):
    #참고로 x가 세로고 y과 x라고 제시되어, y,x 입력 순서를 바꿈
    l, d, y, x = map(int, input().split())
    if (d == 0):  # 가로
        for i in range(l):
            MAP[y-1][x-1+i] = 1
    elif (d == 1):  # 세로
        for j in range(l):
            MAP[y-1+j][x-1] = 1
showStatus()

