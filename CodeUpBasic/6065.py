a = list(map(int, input().split()))
result = list(filter(lambda x: x % 2 == 0, a))
for i in result:
    print(i)
