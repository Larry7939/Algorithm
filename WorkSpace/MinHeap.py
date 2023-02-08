class Minheap:
    def __init__(self):
        self.heap =[]
        self.heap.append(0) #0은 안쓰는 거니까, 그냥 init에서 집어넣어준다.
    def size(self):return len(self.heap)-1 #0은 빼고 계산한 size
    def isEmpty(self): return self.size()==0
    def Parent(self,i): return self.heap[i//2] #어떤 노드 i의 부모노드 구하기
    def Left(self,i): return self.heap[i*2]
    def Right(self,i): return self.heap[i*2+1]
    def display(self):
        print(self.heap[1:])
    def insert(self,n):
        self.heap.append(n) #제일 뒤에 붙이고,
        i = self.size()
        while(i!=1 and n<self.Parent(i)): #1이면 루트노드인 거니까, 그리고 부모보다 큰 동안 계속한다. #여기랑
            self.heap[i]=self.Parent(i) #parent를 내려준다.
            i = i//2 #한단계 올라간다. i가 1이 되거나, 더 큰 녀석을 만날 때까지 계속한다.
            self.heap[i] = n
    def delete(self): #루트를 제거하고, 말단을 그 자리에 앉힌다.
        parent =1
        child =2
        if not self.isEmpty():
            hroot = self.heap[1] #나중에 반환하기 위해 저장해놓는다.
            last = self.heap[self.size()] #가장 말단의 노드를 올릴 것이다.
            while(child<=self.size()):  
                if child<self.size() and self.Left(parent)>self.Right(parent): #여기랑 #아까 뺐던 chile<self.size()조건 다시 넣음.
                    child+=1
                #last가 child보다 크거나 같으면, 종료해준다.
                if last <= self.heap[child]: #여기까지 총 3군데 부등호만 바꿔주면 된다.
                    break
                self.heap[parent] = self.heap[child] #바꿔준다.
                parent =child
                child *= 2  #왼쪽의 인덱스는 2를 곱해준다.
            #child가 self.size보다 커졌다면, parent에 last를 써준다.
            self.heap[parent] = last
            self.heap.pop(-1) #마지막에 있는건 삭제해주고 root를 반환한다.
            return hroot

data = [5,2,3,1,8]
heap = Minheap()
for elem in data:
    heap.insert(elem)
heap.display()
print("삭제 후")
heap.delete()
heap.display()