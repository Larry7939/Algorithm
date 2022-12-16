a =  map(int,input().split())
for i in a:
    if 90<=i<=100:
        print('A')
    elif 70<=i<=89:
        print('B')
    elif 40<=i<=69:
        print('C')
    else:
        print('D')
