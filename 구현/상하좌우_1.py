#start = (1,1)
#L R U D
#지도 밖으로 탈출 불가

#우선 내가 만든 알고리즘의 시간 복잡도가 어느정도일 지 체크해야함.
#N과 계획서를 입력받는다 -> 계획서를 배열에 입력받고, for문을 돌면서 if문으로 각각 어떤 명령인지를 체크해서 좌표를 이동시킨다.
#if문 내부에서는 x좌표 또는 y좌표가 1또는 5를 넘어가지는 않는지 체크한다. (1<=x<=5 and 1<=y<=5)
#최종 좌표를 출력한다.
#시간 복잡도는 O(N)

n = int(input())
a = list(input().split())
x,y=1,1
for i in a:
    if (i == 'L') and (x-1!=0):
        x-=1
    elif (i == 'R') and (x+1!=n+1):
        x+=1
    elif (i== 'U') and (y-1!=0):
        y-=1
    elif (i =='D') and (y+1!=n+1):
        y+=1
print(y,x)