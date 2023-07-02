#BOJ 20164 홀수 홀릭 호석
import sys
num = sys.stdin.readline().rstrip()
#수의 각 자리 숫자 중, 홀수의 개수를 종이에 적는다.
#수가 한 자리이면, 더 이상 아무것도 하지 못하고 종료한다.
#수가 두 자리이면, 2개로 나눠서 합을 구하여 새로운 수로 생각한다.
#수가 세 자리 이상이면, 임의의 위치에서 끊어서 3개의 수로 분할하고 3개를 더한 값을 새로운 수로 생각한다.
answer = []
cnt = 0


#재귀를 활용하여 매번 새로운 수를 전달
def recurOddNumber(num:str,cnt:int):
    length = len(num)
    cnt += getOddNumber(num)
    if length == 1:
        answer.append(cnt)
        return 
    elif length==2:
        recurOddNumber(str(int(num[0])+int(num[1])),cnt)
    elif length>=3:
        #반복문으로 2개의 수를 뽑아서 총 3개의 구역으로 나누도록 함.
        for i in range(1,length-1):
            for j in range(i+1,length):
                recurOddNumber(str(int(num[0:i]) + int(num[i:j]) + int(num[j:])),cnt)


# 문자열에 포함된 홀수의 개수를 반환하는 함수
def getOddNumber(num:str):
    result = 0
    for n in num:
        if int(n)%2!=0:
            result +=1
    return result

recurOddNumber(num,cnt)
print(min(answer),max(answer))