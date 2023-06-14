a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
for i in range(3):
    for j in range(3):
        print(a[i][j],end='')
    print()



a = list(zip(*a[::-1])) # 시계방향 90도 회전
for i in range(3):
    for j in range(3):
        print(a[i][j],end='')
    print()
