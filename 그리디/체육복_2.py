# 테스트 1
# 입력값 〉	5, [2, 4], [1, 3, 5]
# 기댓값 〉	5

# 테스트 2,
# 입력값 〉	5, [2, 4], [3]
# 기댓값 〉	4

n = 3
lost = [3]
reserve = [1]
_reserve = list(set(reserve) - set(lost))
_lost = list(set(lost) - set(reserve))

for r in _reserve:
    if r-1 in _lost:
        _lost.remove(r-1)
    elif r+1 in _lost:
        _lost.remove(r+1)

print(n - len(_lost))