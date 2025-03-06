# 입력부
# N(유제품의 수)
# prices(유제품의 가격)
N = int(input())
prices = []
for _ in range(N):
    prices.append(int(input()))
result = 0
# 1. prices 내림차순 정렬
prices.sort(reverse = True)
# 2. index를 3씩 증가시키면서 내부의 값들을 마지막 원소만 제외하고 result에 합산
for i in range(0, N, 3):
    if i+1 >= N:
        result += prices[i]
        break
    result += (prices[i] + prices[i+1])
print(result)

# 핵심: 최대한 비싼 가격의 유제품을 공짜로 받을 수 있도록 해야한다.