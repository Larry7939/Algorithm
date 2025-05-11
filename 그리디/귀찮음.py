#풀이 횟수 3
#BOJ 16208 귀찮음
import sys
#2 3 4 5
#2 12 - 24
#3 9 - 27
#4 5 - 20
#작은 것부터 하나씩 잘라내는 방식
#막대 길이 정렬 후, 루프를 돌면서, 맨 앞 원소와, 전체에서 이것을 뺀 나머지를 곱해서 answer에 더한다.
n = int(sys.stdin.readline())
lengths = list(map(int,sys.stdin.readline().split()))
lengths.sort()

answer = 0
length_sum = sum(lengths)
for i in range(len(lengths)):
    length_sum = length_sum-lengths[i]
    answer += lengths[i]*length_sum
print(answer)

# 루프 내에서 매번 sum을 구하면 서브테스크 실패.
# 이전에 계산한 값 length_sum-lengths[i]로 갱신해야 시간 내에 실행 완료 가능