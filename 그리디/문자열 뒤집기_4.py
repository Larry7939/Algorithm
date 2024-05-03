s = list(map(int,''.join(input().split())))
length = len(s)

group_0 = 0
group_1 = 0

if s[0] == 0:
    group_0 += 1
else:
     group_1 += 1
     
for i in range(1, length):
    if s[i-1] == 0 and s[i] == 1:
        group_1 += 1
    elif s[i-1] == 1 and s[i] == 0:
        group_0 += 1
print(min(group_0,group_1))