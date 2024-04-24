# N: 쇠막대의 수
# lengths: 쇠막대 길이 리스트
# length_sum: 쇠막대 길이 합
N = int(input())
lengths = list(map(int,input().split()))
lengths.sort(reverse=True)
length_sum = sum(lengths)

result = 0
# legths를 순회하면서 (length_sum-length) * length를 result에 합산
# 자르고 남은 막대 길이 총합(length_sum) 업데이트
for length in lengths:
    result += (length_sum-length) * length
    length_sum -= length
print(result)