a = int(input())
for i in range(1,a+1):
    count=0
    count += str(i).count('3')
    count += str(i).count('6')
    count += str(i).count('9')
    if(count!=0):
        print(('X'*count),end=' ')
    else:
        print(i,end=' ')
    
