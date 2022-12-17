a, r, n = list(map(int, input().split()))
if (n == 0):
    print(0)
else:
    print(a*pow(r,n-1))
