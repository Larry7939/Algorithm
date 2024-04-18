# 숫자 입력
# 0 또는 1일 때에는 더하기, 그 외에는 곱하기 연산 수행
nums = list(map(int,''.join(input().split())))

result = 0
for num in nums:
    if result == 0 or num == 0 or num == 1:
        result += num
    else:
        result *= num
print(result)