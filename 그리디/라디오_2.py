# 현재 주파수 A, 목표 주파수 B
# 즐겨찾기 주파수 개수 N
# 즐겨찾기 주파수 리스트 favorites

# 1. 즐겨찾기 버튼을 사용하지 않는 경우 -> abs(A-B)
# 2. 즐겨찾기 버튼을 사용하는 경우 -> abs(목표 주파수와 가장 가까운 즐겨찾기 주파수 - 목표 주파수) + 1
A, B = map(int,input().split())
N = int(input())
result = [abs(A-B)]

for _ in range(N):
    favorite = int(input())
    result.append(abs(favorite - B) + 1)
print(min(result))