import sys
# 곱하기 혹은 더하기
s = sys.stdin.readline().rstrip()
s = list(map(int,''.join(s)))

answer= s[0]

for i in range(1,len(s)):
    if s[i] <= 1 or answer <= 1:
        answer += s[i]
    else:
        answer *= s[i]
print(answer)