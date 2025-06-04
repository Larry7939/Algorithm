n = int(input())
t = [0] * (n+1)
t[0] = 1
if n>0:
    t[1] = 1

for i in range(2, n+1):
    for j in range(0, i):
        t[i] += t[j] * t[i-j-1]

print(t[n])