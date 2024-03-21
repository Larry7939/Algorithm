# 풀이 횟수 2
N,M,K = map(int,input().split()) #N:배열의 크기 M:더해지는 횟수 K:최대 연속 더하는 횟수
a:list = list(map(int,input().split()))
sum =0
temp = 0
for i in range(1,M+1):
    if i%(K+1)==0:
        temp = max(a)     #i가 K+1의 배수가 될 때마다 두번째로 큰 수를 더해주기 위해서
        a.remove(max(a))  #가장 큰 수를 temp에 임시저장한 다음 a에서 제외시키고, 두번째로 큰 수를 sum에 더해준다.
        sum += max(a)     
        print(f"두번째로 큰 수 더하기 {max(a)}")
        a.append(temp)    #두번째 수를 더했으면, 임시저장된 가장 큰 수를 배열에 다시 넣어준다.
    else:
        print(f"첫번째로 큰 수 더하기 {max(a)}")
        sum+=max(a)       #평상시에는 가장 큰 수를 계속 더해준다.
print(sum)


