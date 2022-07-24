#정수 N입력(0<=N<=23)
# 3이 하나라도 포함되어있는 시각의 개수 출력

count=0
n = int(input())
for i in range(0,n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)