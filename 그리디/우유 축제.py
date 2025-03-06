# 딸기 마시기 규칙
# 딸기우유 -> 초코우유 -> 바나나 우유 -> 딸기 우유
# 딸기우유(0), 초코 우유(1), 바나나 우유(2)
# N개의 가게를 지나면서 마시기 or 지나치기

# 입력부
# N(가게의 수), stores(우유 가게 정보)
milks = [0, 1, 2]
nextMilkToDrink = 0
result = 0
N = int(input())
stores = list(map(int,input().split()))

# 1. 우유 가게 지나가기 
# 2. 가게의 우유를 nextMilkToDrink와 비교
#  true -> result += 1, nextMilkToDrink 업데이트
for store in stores:
    if nextMilkToDrink == store:
        result += 1
        nextMilkToDrink = milks[(nextMilkToDrink + 1) % 3]
print(result)

# 핵심: 인덱스 나머지 규칙 활용