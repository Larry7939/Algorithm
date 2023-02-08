class Maxheap:
    def __init__(self):
        self.heap =[]
        self.heap.append(0) #0은 안쓰는 거니까, 그냥 init에서 집어넣어준다.
    def size(self):return len(self.heap)-1 #0은 빼고 계산한 size
    def isEmpty(self): return self.size()==0
    def Parent(self,i): return self.heap[i//2] #어떤 노드 i의 부모노드 구하기
    def Left(self,i): return self.heap[i*2]
    def Right(self,i): return self.heap[i*2+1]
    def display(self):print(self.heap[1:])
    def insert(self,n):
        self.heap.append(n) #제일 뒤에 붙이고,
        i = self.size()
        while(i!=1 and n>self.Parent(i)): #1이면 루트노드인 거니까, 그리고 부모보다 큰 동안 계속한다.
            self.heap[i]=self.Parent(i) #parent를 내려준다.
            i = i//2 #한단계 올라간다. i가 1이 되거나, 더 큰 녀석을 만날 때까지 계속한다.
            self.heap[i] = n
    def delete(self): #루트를 제거하고, 말단을 그 자리에 앉힌다.
        parent =1
        child =2
        if not self.isEmpty():
            hroot = self.heap[1] #나중에 반환하기 위해 저장해놓는다.
            last = self.heap[self.size()] #가장 말단의 노드를 올릴 것이다.
            while(child<=self.size()): #child가 size보다 작은 동안 계속 돌린다.
                #child가 왼쪽으로 갈지, 오른쪽으로 갈 지 선택해야하기 때문에,
                #만약 왼쪽보다 오른쪽 자식이 더 크면,오른쪽으로 간다. child<self.size()는 없어도 될것 같다.
                if parent*2+1<self.size(): ##self의 right부분이 size보다 작도록 해서 out of range를 피하자
                    if self.Left(parent)<self.Right(parent):
                        child+=1
                #last가 child보다 크거나 같으면, 종료해준다.
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child] #바꿔준다. 비어있는 윗자리를 채우기 위해 올라가는 거임!
                parent =child #parent와 child가 가리키는 곳을 한칸씩 내려준다.
                child *= 2  #왼쪽의 인덱스는 2를 곱해준다.
            #child가 self.size보다 커졌다면, parent에 last를 써준다.
            self.heap[parent] = last
            self.heap.pop(-1) #마지막에 있는건 삭제해주고 root를 반환한다.
            return hroot

def heapSort(data): #data라는 배열을 집어넣는다.
    heap = Maxheap()
    for n in data:
        heap.insert(n)
    for i in range(1,len(data)+1):
        data[-i] = heap.delete()#오름차순으로 정렬하면, data의 끝에서부터 delete한 결과를 집어넣어야한다.
        print(data)

data = [5,3,8,4,9,1,6,2,7]
heapSort(data)
print(data)