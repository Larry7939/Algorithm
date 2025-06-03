# N-Queen 문제

n = int(input())
columns = [False]*n
diag1 = [False]*(2*n-1) # 우하향 대각선
diag2 = [False]*(2*n-1) # 좌하향 대각선

count = 0
def backtracking(row):
    global count
    if row == n:
        count += 1
        return
    for col in range(n):
        
        if columns[col]:
            continue
        if diag1[row-col+n-1] or diag2[row+col]:
            continue
        columns[col] = diag1[row-col+n-1] = diag2[row+col] = True
        backtracking(row+1)
        columns[col] = diag1[row-col+n-1] = diag2[row+col] = False
backtracking(0)
print(count)