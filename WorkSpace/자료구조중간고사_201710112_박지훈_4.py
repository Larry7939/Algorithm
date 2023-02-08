import random
MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[None]*MAX_QSIZE
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self):
        self.front = self.rear
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear]=item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear+MAX_QSIZE-self.front)%MAX_QSIZE
    def get_Cus(self,pos):
        if not self.isEmpty() and pos>0:
            return self.items[(self.front+pos)%MAX_QSIZE]
    def display(self):
        out =[]
        if self.front<self.rear:
            out=self.items[self.front+1:self.rear+1]
        else:
           out=self.items[self.front+1:MAX_QSIZE]\
               +self.items[0:self.rear+1]
        print("[f=%d, r=%d]"%(self.front,self.rear),out)

sim_time = int(input("시뮬레이션 할 최대 시간: "))
cus_per_time = float(input("단위시간에 도착하는 고객 수"))
cus_num=0 #고객 번호
cur_time=1 #현재 시간
cq = CircularQueue() #은행창구
waiting_time=[-1]*sim_time #대기 시간
service_time=0
s_count=0#서비스 받은 고객 수
while cur_time<=sim_time:
    print("현재 시간= %d"%cur_time)
    i = int(random.random()*10)
    if 0<=i<cus_per_time*10: #고객 방문
        print("고객 %d방문"%(cus_num+1))
        waiting_time[cus_num] = 0
        cq.enqueue(cus_num)
        cus_num+=1
    if(cus_num>0 and service_time==0): #servicetime이 0이 되면 다른 고객 서비스 시작
        c = cq.dequeue()
        if not c==None:
            print("고객 %d 서비스 시작"%(c+1),end='')
            s_count+=1
            print("(대기시간 %d분)"%(waiting_time[c]))
            service_time=4        
    if service_time>0:
        for i in range(10):
            if waiting_time[i]!=-1: #아직 들어오지 않은 고객들은 waiting_time이 -1임.
                waiting_time[i]+=1 #누군가가 서비스받는 동안 대기시간 +1
        service_time-=1
    cur_time+=1

total_wait_time=0
for i in range(cus_num):
    total_wait_time+=waiting_time[i]
print("===결과값 출력===")
print("서비스 받은 고객 수 = %d"%s_count)
print("전체 대기시간=%d분"%total_wait_time)
print("서비스 고객 평균 대기시간 =%f분"%(total_wait_time/cus_num))
print("현재 대기고객 수=%d명"%(cus_num-s_count))