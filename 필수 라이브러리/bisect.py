from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print("bisect")
print(bisect_left(a,x))
print(bisect_right(a,x))
print(bisect_right(a,x)-bisect_left(a,x))
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
# '정렬된 리스트'에서 특정 범위에 속하는 원소의 개수를 구하는데 효과적이다.
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6
