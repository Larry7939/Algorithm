import sys
# 입력
s = list(map(int, ''.join(sys.stdin.readline().rstrip())))
s.sort(reverse=True)

result = s[0]
# 메인
for i in range(1, len(s)):
    # 연산 대상이 되는 두 수 중에서 하나라도 0 또는 1이라면, 곱하기보다는 더하는 것이 좋다.
    # 연산 대상 또는 초기 결과값이 1이하일 경우
    if s[i] <= 1 or result <= 1:
        #결과값에 해당 수를 더한다.
        result += s[i]
    #연산 대상이 2이상일 경우
    else:
        result *= s[i]

# 출력
print(result)
