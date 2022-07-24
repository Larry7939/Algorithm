# N%K!=0일 때 or ==0일 때
# N을 1로 만드는 1,2번 과정의 최소 필요 횟수

#풀이방법2
#N이 K의 배수가 되도록 먼저 한꺼번에 뺀 다음에 연산하는 방법

n,k = map(int,input().split())
result = 0

while True:
    #N==K로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k)*k #<- 이건 나머지를 털어내는 작업이다. N//K로 몫을 골라내고 여기에 K를 곱해서 나머지를 제외한, K의 배수인 target을 도출해냈다.
    result += (n-target) #따라서 result에 미리 나머지를 더해놓는다. 
    n = target
    #N이 K보다 작아지면 반복문 탈출
    if n<k: 
        break
    #K로 나누기
    result += 1 #한번 나누기 연산을 할 때마다 result + 1
    n//=k
result += (n-1) #n이 0이 아닌 1이 되는 것이 목표이므로 n-1
print(result)


