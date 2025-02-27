# 1 + (2+3)
# 1,+,(,2,+,3,)
# 2+3 -> 2 3 + -> 5
# 계산 우선순위

# 사칙 연산
# 1. 곱셈, 나눗셈을 우선 계산
# 2. 수식 문자열을 맨 앞에서부터 검사하면서 우선순위가 높은 연산자로 우선 연산
# 3. 덧셈 뺄셈 연산

# 괄호 계산
# 1. 열린 괄호를 만났을 때, 닫힌 괄호가 나올 때 까지의 수식 우선 계산
# 2. 1번 계산 결과로 수식의 괄호 수식을 대체 (replace)

# 중복 괄호 -> 열린 괄호를 만났을 때, 만약 열린 괄호를 한 번 더 만난 경우
# 닫힌 괄호까지의 수식을 재귀함수의 매개변수로 전달하여 결과 반환
# 반환받은 결과로 괄호 수식을 대체

operators = ["+","-","*","//"]
high_priority_operators = ["*","//"]
selected_high_priority_operator = []
s = input().strip()


for i in range(len(s)):
    if s[i] in high_priority_operators:
        selected_high_priority_operator.append(s[i]) # 우선 연산자 선정
        temp_for_replace = str(s[i-1]) + s[i] + str(s[i+1])
        