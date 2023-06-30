#BOJ 20164 홀수 홀릭 호석
import sys
from itertools import combinations
num = sys.stdin.readline().rstrip()
#수의 각 자리 숫자 중, 홀수의 개수를 종이에 적는다.
#수가 한 자리이면, 더 이상 아무것도 하지 못하고 종료한다.
#수가 두 자리이면, 2개로 나눠서 합을 구하여 새로운 수로 생각한다.
#수가 세 자리 이상이면, 임의의 위치에서 끊어서 3개의 수로 분할하고 3개를 더한 값을 새로운 수로 생각한다.
answer = []
result = 0
def createNewString(num:str,index_list:list):
    print(index_list)
    result = 0
    s = ''
    for i in range(0,index_list[0]):
        s += num[i]
    
    print(s,end=' ')
    result += int(s)
    s = ''
    for i in range(index_list[0],index_list[1]):
        s += num[i]
    print(s,end=' ')
    result += int(s)
    s = ''
    for i in range(index_list[1],len(num)):
        s += num[i]
    print(s)
    result += int(s)
    print(result)
    return str(result)

#재귀를 활용하여 매번 새로운 수를 전달
def recurOddNumber(num:str):
    global result
    length = len(num)
    result += getOddNumber(num)
    if length == 1:
        print("length == 1")
        answer.append(result)
        result = 0
        return 
    elif length==2:
        print("length == 2")
        recurOddNumber(str(int(num[0])+int(num[1])))
    elif length>=3:
        print("length >= 3")
        a = list(combinations(range(length),2))
        for i in a:
            if i[0] != 0:
                b = createNewString(num,i)
                recurOddNumber(b)
# 문자열에 포함된 홀수의 개수를 반환하는 함수
def getOddNumber(num:str):
    result = 0
    for n in num:
        if int(n)%2!=0:
            result +=1
    return result

recurOddNumber(num)
print(result)
print(answer)