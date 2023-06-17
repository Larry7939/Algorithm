import sys
s = sys.stdin.readline().rstrip()
# 111110001111 -> 1
# 1100110011 -> 2
answer = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        answer += 1

print((answer+1)//2) 
#1010, 0101과 같은 반례에서는 3이 나오게 되는데, 이렇게 홀수가 나오게 되는 경우, 2가 아닌 1이 출력되어버린다.
#+1을 해주면 홀수인 경우와 짝수인 경우 모두 몫연산에 의한 오출력을 피할 수 있다.