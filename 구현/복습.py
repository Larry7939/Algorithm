import sys
n = int(sys.stdin.readline())
h = n+1
m = 60
s = 60
answer = 0
for i in range(h):
    for j in range(m):
        for k in range(s):
            if '3' in str(i)+str(j)+str(k):
                print(f"{i}:{j}:{k}")
                answer += 1
print(answer)