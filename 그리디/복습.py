import sys
# 큰 수의 법칙
n,m,k = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
result = 0
# 가장 큰 수를 가장 많이 더하도록 해야 함.
# 6+6+6+5+6+6+6+5 m = 8, k = 3, m//(k+1) = 2, m%k = 2
# 첫번째로 큰 수를 더하는 횟수 : m - m//(k+1) = 6
# 두번째로 큰 수를 더하는 횟수 : m//(k+1) = 2

# 6+6+6+5+6+6+6+5+6 m = 9, k = 3, m//(k+1) =3, m%k = 0
# 첫번째로 큰 수를 더하는 횟수 : m - m//(k+1) = 7
# 두번째로 큰 수를 더하는 횟수 : m//(k+1) = 2
second_num = nums[-2]
second_num_count = m//(k+1)
first_num = nums[-1]
first_num_count = m-second_num_count

result = first_num*first_num_count + second_num*second_num_count
print(result)

# 최대값과 두번째로 큰 값을 일일이 더하는 것이 아닌, 몫과 나머지의 관계를 이용해
# 최대값과 두번째로 큰 값이 등장하는 횟수를 구할 수 있는 식을 만드는 것이 핵심