# N: 배열의 크기
# M: 숫자가 더해지는 횟수
# K: 특정 인덱스의 수를 연속으로 더할 수 있는 횟수
N,M,K = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort(reverse=True)

b = M // (K+1) # 두번째로 큰 수가 더해지는 횟수
a = M - b # 가장 큰 수가 연속으로 더해지는 횟수
print(numbers[0] * a + numbers[1] * b)

# N = 5, M = 8, K = 3
# numbers = [2, 4, 5, 4, 6]
# 6 6 6 5 6 6 6 5
# 46

# N = 5, M = 7, K = 3
# numbers = [2, 4, 5, 4, 6]
# 6 6 6 5 6 6 6
# 41

# N = 5, M = 3, K = 3, 
# numbers = [2, 4, 5, 4, 6]
# 6 6 6
# 18
