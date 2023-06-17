#BOJ 18312 시각
import sys
#정수 N입력(0<=N<=23)
# a가 하나라도 포함되어있는 시각의 개수 출력
# 반례 - a가 0인 경우에 대한 고려 필수
count=0
n,a = map(int,sys.stdin.readline().split())
for i in range(0,n+1):
    for j in range(60):
        for k in range(60):
            h = str(i)
            m = str(j)
            s = str(k)
            if i < 10:    
                h = '0' + h
            if j < 10:
                m = '0' + m
            if k < 10:
                s = '0' + s
            
            result = h+m+s
            if str(a) in result:
                count+=1
print(count)
