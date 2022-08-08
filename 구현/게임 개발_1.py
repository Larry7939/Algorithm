#NxM크기의 직사각형 장소
#각 칸은 육지 또는 바다, 바다로는 갈 수 없음
#동서남북 중 한쪽을 바라봄
#(A,B) A는 행, B는 열

#왼쪽으로 회전 후 가본 적이 없으면 이동 / 가본 적이 있으면 왼쪽 회전만하고 1단계로 돌아감
#네 방향 모두 가본 칸이거나 바다면, 바라보는 방향은 유지한 채로 한 칸 뒤로 가고 1단계로 돌아감 BUT, 뒤가 바다라면 움직임을 멈춤
#메뉴얼에 따라 캐릭터를 이동시키고 방문한 칸의 수를 출력
#북(0) 서(3) 남(2) 동(1) 

#왼쪽으로 돌면서 갈 방향을 정해야한다.

steps = [(0,-1),(-1,0),(0,1),(1,0)]#좌(북),상(동),우(남),하(서)
n,m = map(int,input().split()) #n,m 맵 크기
a,b,d = map(int,input().split()) #캐릭터가 있는 칸의 좌표와 바라보는 방향
map1 = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    map1[i]= list(map(int,input().split()))
dx=0
dy=0
history = []
count=1
turn_time=0
current = (a,b)

def left_turn():
    global d
    if d==0: d=3
    else: d-=1
while True:
    left_turn()
    dy=a+steps[d][0] #보고있는 방향에 따라 다르게 움직인다
    dx=b+steps[d][1] #보고있는 방향에 따라 다르게 움직인다
    if map1[dy][dx]==0 and (dx,dy) not in history: #왼쪽으로 돌다가 간 적이 없는 육지가 나오면 이동
        map1[dy][dx] = 1
        history.append((dx,dy))
        a+=steps[d][0]
        b+=steps[d][1]
        count+=1        #가본 장소 +1
    else:               #왼쪽으로 돌았는데 가본 칸이거나 바다인 경우, turn time만 증가시킴
        turn_time+=1
    if turn_time==4: #전부 돌아도 갈 곳이 없는 경우 뒤로 이동
        dy=a-steps[d][0]
        dx=b-steps[d][1]
        if map1[dy][dx]==0: #dy,dx로 체크해보고 갈 수 있는 곳이면 a,b를 변경시켜서 이동
            a-=steps[d][0]
            b-=steps[d][1]
        else:
            break           #갈 수 없다면 동작 종료
        turn_time=0         #뒤로 간 다음에 새로 방향을 탐색할 수 있도록 turn_time=0
print(count)