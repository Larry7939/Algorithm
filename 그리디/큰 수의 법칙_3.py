#N = 5, M = 8, K = 3
#6+6+6+5+6+6+6+5 = 46 -> M//(K+1) == 0인 경우, 즉, 나뉘어 떨어지는 경우


#N = 5, M = 9, K = 3
#6+6+6+5+6+6+6+5+6 = 52 -> M//(K+1) != 0인 경우, 즉, 나뉘어 떨어지지 않는 경우

#위 두가지의 경우 각 수가 등장하는 횟수 공식
#first = M-M//(K+1)
#second = M//(K+1)

N,M,K = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
first_formula = (M-M//(K+1))
second_formula = M//(K+1)
answer = a[-1]*first_formula + a[-2]*second_formula
print(answer)
