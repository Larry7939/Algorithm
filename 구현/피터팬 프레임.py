# BOJ 3054 피터팬 프레임
import sys
# 피터팬 프레임 - X
# 웬디 프레임 - *
# 단어의 3의 배수 위치의 알파벳은 웬디 프레임, 나머지는 피터팬 프레임으로 장식
# 프레임이 겹치는 경우엔 웬디 프레임을 위에 장식
word = str(sys.stdin.readline()).rstrip()

frame_hieght = 5
frame_width = 5
length = len(word)

def createRow1(row1):
    #한 단위를 .#..로 규정
    #word의 길이를 반복문으로 돌다가, 만약 3으로 나누어떨어진다면 .*..를 추가
    for i in range(1,length+1):
        if i %3 == 0:
            row1 += ".*.."
        else:
            row1 += ".#.."
    return row1
def createRow2(row2):
    for i in range(1,length+1):
        if i %3 == 0:
            row2+= "*.*."
        else:
            row2 += "#.#."
    return row2
def createRow3(row3):
    for i in range(1,length+1):
        if i %3 == 0: #인덱스가 3의 배수인 경우,
            row3 = row3[:len(row3)-1]  #웬디 프레임의 우선순위가 높으므로 맨 마지막 프레임 삭제
            row3+= "*." +word[i-1] + ".*"
        else:
            if i==1: #첫번째인 경우
                row3 += "#." + word[i-1] +".#" 
            else:
                if row3[-1] == "*": #앞에 웬디 프레임이 있는 경우
                    row3 += "." + word[i-1] +".#"
                else:
                    row3 += "." + word[i-1] +".#"
    return row3
row1 = row2 = "."
row3 = ""

row1 = createRow1(row1)
row2 = createRow2(row2)
row3 = createRow3(row3)
print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

#단어의 한 글자당 출력할 행 한 단위를 올바르게 정하는 것, 웬디 프레임('*')의 우선순위가 피터팬 프레임('#')보다 앞서게 하는 것이 핵심.