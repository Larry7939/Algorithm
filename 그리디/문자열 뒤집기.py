# 0과 1로만 이루어진 문자열 S의 모든 숫자를 전부 같게 하는 것이 목표
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는다.

# 문자열 입력
s = list(input())
s_for_zero = s.copy()
s_for_one = s.copy()
# 0을 뒤집는 경우
# 1을 뒤집는 경우
# 위 두가지 경우에 대해서 모든 숫자가 동일한 지 검사하고 연산 횟수를 비교 후 최솟값 출력

zero_count = 0
one_count = 0
# 0을 뒤집는 경우
for i in range(len(s_for_zero)):
    if s_for_zero[i] == "0":
        while i < len(s_for_zero) and s_for_zero[i] != "1":
            s_for_zero[i] = "1"
            i += 1
        zero_count += 1   

# 1을 뒤집는 경우
for i in range(len(s_for_one)):
    if s_for_one[i] == "1":
        while i < len(s_for_one) and s_for_one[i] != "0":
            s_for_one[i] = "0"
            i += 1
        one_count += 1   

print(min(zero_count, one_count))


# 10011100000
# 000110000
# 1000001
# 0100101