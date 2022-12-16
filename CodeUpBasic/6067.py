a = map(int,input().split())
for i in a:
    if i%2==0 and i<0:
        print('A')
    elif i%2==0 and i>0:
        print('C')
    elif i%2!=0 and i<0:
        print('B')
    else:
        print('D')
