def insertion_sort(A):
    n = len(A)
    for i in range(1,n): #key값을 1부터 n-1까지 변환시켜가면서 진행한다.
        key = A[i] #key는 A[i]
        j = i-1 #j는 i-1부터, 계속 감소시킨다.
        #j가 0보다 크거나 같은 경우에, 계속 감소시키면서 진행하고, A[j]가 key보다 작아지면 끝낸다.
        #j가 -1이 되면 A의 0번째가 key값이 되는 것이고, j가 집어넣은 다음에 while문에서 빠져나왔으면, 원래 j였던 값에 key값을 집어넣는다.
        while j>=0 and A[j]>key: 
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
        printStep(A,i)
def printStep(array,val):
    print("   Step %d = "%val,end='')
    print(array)
data = [5,3,8,4,9,1,6,2,7]
print("Original : ",data)
insertion_sort(data)
print("Insertion : ",data)
