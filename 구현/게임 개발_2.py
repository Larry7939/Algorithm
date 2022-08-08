#NxM크기의 직사각형 장소
#각 칸은 육지 또는 바다, 바다로는 갈 수 없음
#동서남북 중 한쪽을 바라봄
#(A,B) A는 행, B는 열

#왼쪽으로 회전 후 가본 적이 없으면 이동 / 가본 적이 있으면 왼쪽 회전만하고 1단계로 돌아감
#네 방향 모두 가본 칸이거나 바다면, 바라보는 방향은 유지한 채로 한 칸 뒤로 가고 1단계로 돌아감 BUT, 뒤가 바다라면 움직임을 멈춤
#메뉴얼에 따라 캐릭터를 이동시키고 방문한 칸의 수를 출력
#북(0) 서(3) 남(2) 동(1) 

#왼쪽으로 돌면서 갈 방향을 정해야한다.

def turn_left():
    global direction
    direction -=1
    if direction ==-1:
        direction = 3

n,m = map(int,input().split()) #n-세로 m-가로
map1 = [[0 for _ in range(m)] for _ in range(n)]
x,y,direction = map(int,input().split())
for i in range(n):
    map1[i] = list(map(int,input().split()))

dx =[-1,0,1,0] #북(x-1)/서(y-1)/남(x+1)/동(y+1)
dy =[0,-1,0,1] #ex) dx[0],dy[0]은 북쪽을 바라볼 때 움직이는 동작
turn_count=0
count =1
nx,ny=0,0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if map1[ny][nx] ==0:
        x+=dx[direction]
        y+=dy[direction]
        map1[y][x]=1
        count+=1
    else:
        turn_count+=1
    if turn_count==4:
        nx=x-dx[direction]
        ny=y-dx[direction]
        if map1[ny][nx]==0:
            x-=dx[direction]
            y-=dy[direction]
            map1[y][x]=1
            count+=1
            turn_count=0
        else:
            break
#왼쪽으로 돌고 nx,ny를 이용해서 map1[nx][ny]에 갈 수 있는지를 체크하고, 갈 수 있다면 x,y변경 / 갈 수 없다면 turn_count만 증가시키고 반복
#turn_count가 4가 된다면 뒤로 가야한다. 뒤로 갈 수 있는지를 체크하기 위해 nx,ny로 체크하고 갈  수 있으면 x,y변경시키고 turn_count=0, 없으면 break로 동작 중지 
print(count)