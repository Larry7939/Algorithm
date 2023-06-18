import sys
# BOJ 11866 요세푸스 문제 0
n, k = map(int, sys.stdin.readline().split())
a = list(range(1, n+1))
x = 0
result = []
for _ in range(n):
    x += k-1
    if x >= len(a):
        x =  x % len(a)
    result.append(str(a.pop(x)))


print('<'+', '.join(result)+'>')
