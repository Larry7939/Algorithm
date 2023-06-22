#BOJ 16922 로마 숫자 만들기
import sys, itertools
def romanToNumber(s):
    sum = 0
    for i in s:
        if i == 'I':
            sum+=1
        elif i == 'V':
            sum+=5
        elif i=='X':
            sum+=10
        elif i=='L':
            sum+=50
    return sum


n = int(sys.stdin.readline())
numbers = ['I','V','X','L']
a = list(itertools.combinations_with_replacement(numbers,n))
result = []
for i in a:
    result.append(romanToNumber(i))
result = set(result)
print(len(result))

#단순하게 list(itertools.combinations_with_replacement(numbers,n))만을 이용해서 구하면, 구성 로마 문자는 다르더라도 숫자는 같은 경우가 포함되어버린다.
#서로 다은 수의 개수를 구하기 위해 직접 sum을 만들고 set으로 중복을 삭제하는 방식을 사용