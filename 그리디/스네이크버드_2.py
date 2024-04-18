# 과일 개수 N, 최초 길이 L
# 과일 높이 리스트 heights

N, L = map(int,input().split())
heights = list(map(int,input().split()))
heights.sort()
for h in heights:
    if L >= h:
        L += 1
    else:
        break
print(L)