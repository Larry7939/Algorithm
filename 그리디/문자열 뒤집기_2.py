import sys
s = list(map(int,sys.stdin.readline().rstrip()))

count0 = 0 #0이 연속된 부분
count1 = 0 #1이 연속된 부분

#첫번째 정수는 곧바로 연속된 부분으로 추가
if s[0] == 0:
    count0 += 1
else:
    count1 += 1

#정수를 순서대로 탐색하며, 연속된 정수가 다른 정수로 바뀔 때, 연속된 부분의 개수 추가
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == 0:
            count0 += 1
        else:
            count1 += 1

print(min(count0,count1))


