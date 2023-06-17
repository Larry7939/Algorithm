#BOJ 7568 덩치
import sys
#덩치 - (몸무게,키)
#몸무게와 키 모두 큰 경우 -> 덩치가 더 크다
n = int(sys.stdin.readline())
students = []
for _ in range(n):
    w,h = map(int,sys.stdin.readline().split())
    students.append((w,h))

#덩치 비교 함수 작성
#1이 크면 True, 2가 크면 False
def compareSize(weight1,hegiht1,weight2,height2):
    if weight1 > weight2 and hegiht1 > height2:
        return True
    elif weight1 < weight2 and hegiht1 < height2:
        return False
    else:
        pass


result = [1]*n
for i in range(n):
    w,h = students[i][0],students[i][1]
    for j in range(n):
        if compareSize(w,h,students[j][0],students[j][1]) == False: #본인보다 덩치가 큰 사람의 수를 세기
            result[i] += 1
print(*result)