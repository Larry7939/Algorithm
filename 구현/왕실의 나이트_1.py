#수평 두 칸 이동 후 수직 한 칸 이동
#수직 두 칸 이동 후 수평 한 칸 이동
#나이트가 이동할 수 있는 경우의 수 출력
#행(1~8) 열(a~h) #97~104

count =0 #경우의 수
start = input() #출발지점
 
def vhMove(): #수직-수평
    global count
    #위로 이동
    if int(start[1])-2>0 and ord(start[0])+1<105: #상/우
        count+=1
    if int(start[1])-2>0 and ord(start[0])-1>96: # 상/좌
        count+=1
    #아래로 이동
    if int(start[1])+2<9 and ord(start[0])+1<105: #상/우
        count+=1
    if int(start[1])+2<9 and ord(start[0])-1>96: # 상/좌
        count+=1

def hvMove(): #수평-수직
    global count
    #좌로 이동
    if int(start[1])-1>0 and ord(start[0])-2>96: #좌/상
        count+=1
    if int(start[1])+1<9 and ord(start[0])-2>96: # 좌/하
        count+=1
    #우로 이동
    if int(start[1])-1>0 and ord(start[0])+2<105: #우/상
        count+=1
    if int(start[1])+1<9 and ord(start[0])+2<105: #우/하
        count+=1
vhMove()
hvMove()
print(count)