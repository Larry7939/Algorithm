# def sequential_search(A,key,low,high):
#     for i in range(low,high+1):
#         if A[i]==key:
#             return i
#         printStep(A,i)
#     return None
# def printStep(array,val):
#     print("   Step %d = "%val,end='')
#     print(array)
# data = [5,3,8,4,9,1,6,2,7]
# print("output: %d"%sequential_search(data,1,0,len(data)))

def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                bChanged = True
        if not bChanged:
            break
#이진탐색은 정렬되어있어야 사용할 수 있기때문에, bubble sort로 정렬해놓고 쓴다.
def binary_search(A,key,low,high):
    step = 0
    while low<=high:
        step+=1
        printStep(A,step)
        middle = (low+high)//2
        print("Middle Value: ",middle)
        if key == A[middle]:
            return middle
        elif key>A[middle]:
            low = middle+1
        elif key<A[middle]:
            high = middle-1
    return None
def printStep(array,val):
    print("   Step %d = "%val,end='')
    print(array)
data = [5,3,8,4,9,1,6,2,7]
bubble_sort(data)
print("output:",binary_search(data,1,0,len(data)))