#BOJ 17413 단어 뒤집기2
import sys

#알파벳 소문자(a~z), 숫자, 공백, 특수문자('<','>')
#문자열의 시작과 끝은 공백이 아니다.
#'<'와 '>'가 문자열에 있는 경우, 번갈아가며 등장하고, '<'이 먼저 등장. 두 문자의 개수는 같아야함.

# 태그 - '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열. '<','>' 사이에는 알파벳 소문자와 공백만 있다.
# 단어 - 알파벳 소문자와 숫자로 이루어진 부분 문자열, 연속하는 두 단어는 공백 하나로 구분한다.
# 태그와 단어 사이에는 공백이 없다.


# '<'가 나오면 '>'가 나올 때까지 is_tag_opened = True
# '>가 나오면 is_tag_opened = False
# 

word_list = str(sys.stdin.readline().rstrip())
is_tag_opened = False
result = ''
stack = []
for word in word_list:
    if word == '<':  #열린 괄호가 나오면, 이전의 단어들을 전부 뒤집어서 출력
        is_tag_opened = True
        for _ in range(len(stack)):
            result += stack.pop()
        stack.append(word)
    elif word == '>': #닫힌 괄호가 나오면, 태그 내의 단어들은 뒤집지 않고 출력
        is_tag_opened = False
        stack.append(word)
        for _ in range(len(stack)):
            result += stack.pop(0)
    elif is_tag_opened == False and word ==' ': #태그 밖의 공백을 만나는 경우, 단어를 구분하는 공백이므로 뒤집어서 출력 후, 구분하는 공백' '추가
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
    else:
        stack.append(word)
if len(stack) != 0:
    stack.reverse()
    print(result,end='' )
    print(''.join(stack))
else:
    print(result)