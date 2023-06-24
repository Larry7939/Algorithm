# BOJ 2535 아시아 정보올림피아드
import sys


# 학생 수 제한 x
# 성적 순서대로 세 명에게만 금,은,동메달 수여
# 동점자는 없다.
# 나라별 배달 수는 최대 두 개이다.

# 입력
# 대회참가 학생 수 N (3<=N<=100)
# 국가번호, 학생 번호, 성적

# 출력
# 금, 은, 동메달 순서대로 학생정보(국가번호, 학생번호) 출력

# 학생 정보 리스트 작성
# 입력 받은 학생 정보를 점수 순서대로 정렬.
# 상을 받은 학생이 속한 국가의 수가 이미 2이상인 경우를 체크
def checkRewardNation(reward:list,nation_num):
    if reward.count(nation_num) >= 2:
        return False
    else:
        return True

info_list = dict()
n = int(sys.stdin.readline())
for _ in range(n):
    nation_num, student_num, score = map(int, sys.stdin.readline().split())
    info_list[(nation_num, student_num)] = score
info_list = sorted(info_list.items(), key=lambda item: item[1],reverse=True)

reward = []
count = 0
for info in info_list:
    if count == 3:
        break
    if checkRewardNation(reward,info[0][0]):
        reward.append(info[0][0])
        print(info[0][0], info[0][1])
        count +=1
    else:
        continue