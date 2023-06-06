#BOJ 9237 이장님 초대
import sys
input=sys.stdin.readline

n = int(input()) # 묘목의 수

tree = list(map(int, input().split()))
tree.sort(reverse=True)
# 가장 성장이 오래 걸리는 묘목부터 심기
max_time = 0
for i in range(n):
    max_time = max(max_time,tree[i] + i + 1) # 심는 데에 걸리는 시간 + 심는 날짜 + 심는 데에 걸리는 시간 1
print(max_time+1) # 다 심고 난 다음 날에 초대하므로 + 1