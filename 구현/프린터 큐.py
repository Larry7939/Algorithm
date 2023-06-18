#BOJ 1966 프린터 큐
import sys
from collections import deque
import copy
# 큐의 가장 앞에있는 문서의 '중요도' 확인
# 나머지 문서들 중 현재 문서보다 '중요도'가 높은 문서가 있다면, 현재 문서를 인쇄하지 않고,
# 큐의 가장 뒤로 재배치
# OR 바로 인쇄
# 중요도는 숫자가 클 수록 높다

# 테스트 케이스의 수
t = int(sys.stdin.readline())

# 우선순위가 밀리는 경우 뒤로 보내는 함수
def delayPriority(dq:deque,x):
    dq.popleft()
    dq.append(x)
def checkPriority(dq:deque,x):
    for file in dq:
        if x[1] < file[1]:
            return False
    return True
files = deque()
for _ in range(t):
    count = 0
    files.clear()
    n,m = map(int,sys.stdin.readline().split()) #각각 문서의 개수/몇번째로 인쇄되는지 알고싶은 문서의 인덱스
    temp = list(map(int,sys.stdin.readline().split()))
    for i in range(len(temp)):
        files.append((i,temp[i]))
    goal = files[m]


    for file in copy.deepcopy(files):
        while True:
            if checkPriority(files,files[0]):
                a = files.popleft()
                count += 1
                if a == goal:
                    print(count)
                    break
            else:
                delayPriority(files,files[0])
        break


#인덱스와 값을 함께 튜플 형태로 dq에 넣어야한다.
#값이 같은 경우가 있고, 인덱스도 계속해서 변하기 때문에, 둘 중 하나로만 판별하기에는 무리가 있다.
#goal에 찾고자 하는 인덱스와 값을 넣는다.
#files를 반복하면서, 내부 반복문에서는 특정 파일보다 중요도가 높은 것이 있는지 확인한다.
#중요도가 높은 것이 있다면, delayPriority를 호출해서 뒤로 보낸다.
#그렇지 않다면, 즉시 인쇄하고, 이것이 goal과 일치하는지를 확인한다. count를 증가시킨다.
#일치한다면 count를 print하고 종료한다.