# BOJ 1448 삼각형 만들기
import sys
# 입력부
# 빨대의 개수 n 입력
# 빨대의 길이 3개 입력
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

# 정렬 - nlogn
# 2초 -> 2*10^7
# 3중 반복문 사용 풀이 O(n^3) -> 10^18 이므로 2*10^7을 초과한다
# O(nlogn) -> 10^7

# 정렬한 다음 
a.sort() # - O(nlogn)
answer = -1
while len(a) >= 3: # - O(n)
    # a+b>c를 만족하는지를 확인.
    # 만족 시 3개의 합 구하기
    if a[-3]+a[-2] > a[-1]:
        answer = a[-3]+a[-2]+a[-1]
        break
    # 불만족 시 c를 pop하고 3개의 가장 큰 값으로 위 과정 반복
    else:
        a.pop()
print(answer)

#총 시간 복잡도 O(nlogn)