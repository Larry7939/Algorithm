def quick_sort(A,left,right):
    if left<right:
        print(A)
        q=partition(A,left,right) #피봇을 기준으로 해서 완쪽은 피벗보다 작은 값, 오른쪽은 큰 값이 있는 위치를 찾아야한다.
        quick_sort(A,left,q-1) #그 위치를 partition이라고 한다. 그것을 q가 받아온다.
        quick_sort(A,q+1,right) #열심히 순회해서, 피벗이 들어갈 중간 지점을 반한해주면, 그걸 기반으로 해서 좌우를 순환호출 한다.
def partition(A,left,right):
    low = left+1
    high = right
    pivot = A[left] #그림 참고
    while low<=high:
        while low<= right and A[low]<pivot: #A[low]가 pivot보다 작은 동안 진행
            low+=1
        while high>=left and A[high]>pivot:#A[high]가 pivot보다 큰 동안 진행
            high-=1
        if low<high: #위의 while문이 전부 진행 돼서 멈추면, high랑 low를 바꿔준다.
            A[low],A[high] = A[high],A[low]
    A[left],A[high]=A[high],A[left] #left(pivot)랑 high번째 원소를 바꾸고, high를 return한다.
    return high
data = [5,3,8,4,9,1,6,2,7]
quick_sort(data,0,len(data)-1)
print(data)