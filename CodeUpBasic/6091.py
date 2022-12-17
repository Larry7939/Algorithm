def lcm(a, b, c):
    for i in range(max(a, b, c), (a*b*c)+1):
        if (i % a == 0 and i % b == 0 and i % c == 0):
            return i


a, b, c = map(int, input().split())
print(lcm(a,b,c))
