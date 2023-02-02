# BOJ 14247 나무 자르기
import sys
# 입력부
# 나무의 개수 N 입력
# 첫 날 나무 길이 Hi 입력
# 나무의 성장 길이 Ai 입력
N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
I = list(range(N))  # 나무의 인덱스

I = sorted(I, key=lambda i: A[i])  # 성장 폭에 따라 나무의 인덱스 정렬
ans = 0
# 성장이 더딘 나무 -> 성장 폭이 큰 나무 순서대로 잘라야함.
for i in range(N):
    idx = I[i]  # i번째 날에 벨 나무의 인덱스
    ans += H[i] + i*A[idx]
print(ans)
