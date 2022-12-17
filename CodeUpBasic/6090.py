a,m,d,n = list(map(int,input().split()))

if(n==0):
    print(a)
for i in range(n-1):
    a = a*m+d
print(a)