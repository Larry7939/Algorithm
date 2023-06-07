#BOJ 1461 도서관
#돌아가는 비용을 최소화해야함.
# 1. 음과 양의 영역을 오가선 안된다. -> 부호가 같은 것들끼리 한 묶음
# 2. 가장 멀리 있는 책을 마지막에 가져다 놓아야 한다.
# 3. 가장 멀리 있는 책은 두번째로 멀리있는 책과 묶음으로 가져다 놓아야 한다.
import sys
n,m = map(int,sys.stdin.readline().split())
books = list(map(int,sys.stdin.readline().split()))
answer = 0
book_plus = [book for book in books if book>0]
book_minus = [-book for book in books if book<0]
book_plus.sort(reverse=True)
book_minus.sort(reverse=True)

#한 쪽 배열이 비어있다면, 0으로 지정
if len(book_plus) == 0:
    book_plus = [0]
elif len(book_minus) == 0:
    book_minus = [0]

#최대값이 둘 중 어디에 있는지를 가려야한다.
#max_book = "plus" or "minus"
if book_plus[0] < book_minus[0]:
    max_book = "minus"
else:
    max_book = "plus"

#최대값이 있는 쪽은, 맨 앞 묶음에 * 2를 하지 않아도 된다.
if max_book == "minus":
    answer += book_minus[0]
    for i in range(m,len(book_minus),m):
        answer += book_minus[i]*2
    for j in range(0,len(book_plus),m):
        answer += book_plus[j]*2
elif max_book == "plus":
    answer += book_plus[0]
    for i in range(m,len(book_plus),m):
        answer += book_plus[i]*2
    for j in range(0,len(book_minus),m):
        answer += book_minus[j]*2
print(answer)

#잘못된 경로
# -39 -37 -29 -28 -6 2 11
# 2, 11 -> 11 + 11(돌아가기) = 22
# -6, -28 -> 28 + 28(돌아가기) = 28
# -29, -37 -> 37 + 37(돌아가기) = 74
# -39 -> 39
#50 + 113 = 163

#옳은 경로
# 2, 11 -> 11 + 11(돌아가기) = 22
# -6 -> 6+6(돌아가기) = 12
# -28 -29 -> 29 + 29(돌아가기) = 58
# -37, 39 -> 39
#22+12+58+39 = 131