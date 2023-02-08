def merge_sort(A,left,right):
    print(A[left:right+1])
    if left<right:
        mid = (left+right)//2
        merge_sort(A,left,mid)
        merge_sort(A,mid+1,right) #반을 나눠서 왼쪽, 오른쪽을 정렬한다. 그 안에서도 좌우를 정렬한다.
        merge(A,left,mid,right)
def merge(A,left,mid,right): #left~mid까지, mid+1~right까지는 정렬이 되어있다고 생각한 다음, merge한다.
    global sorted#sorted라는 배열에 정렬된 결과를 집어넣을 것이다.
    #i와 j는 좌우 배열의 인덱스이고, k는 정렬될 배열의 인덱스이다.
    k=left#왼쪽부터 시작
    i=left#왼쪽부터 시작
    j=mid+1#오른쪽부터 시작
    while i<=mid and j<=right: #기본적인 조건
        if A[i]<=A[j]:
            sorted[k] = A[i]
            i,k = i+1,k+1
        else:
            sorted[k] = A[j]
            j,k = j+1,k+1
    if i>mid: #i를 계속 증가시키다가 i가 mid보다 커지면, j의 나머지 애들은 다 sorted뒤에 그대로 넣으면 된다.
        sorted[k:k+right-j+1] = A[j:right+1]
    else: #반대의 경우라면 i에 있는 원소들을 뒤에 넣는다.
        sorted[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1]=sorted[left:right+1]
data = [5,3,8,4,9,1,6,2,7]
sorted = [0]*len(data)
merge_sort(data,0,len(data)-1)
print(data)